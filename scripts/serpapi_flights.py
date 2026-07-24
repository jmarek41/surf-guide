#!/usr/bin/env python3
"""Private-key-safe SerpAPI Google Flights helper."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def load_key() -> str:
    key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if key:
        return key

    secret_file = Path("data/secrets/serpapi.env")
    if secret_file.exists():
        for line in secret_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("SERPAPI_API_KEY="):
                return line.split("=", 1)[1].strip()
    legacy_secret_file = Path("data/secrets/serpapi-key")
    if legacy_secret_file.exists():
        key = legacy_secret_file.read_text(encoding="utf-8").strip()
        if key:
            return key
    raise SystemExit(
        "SerpAPI key missing. Set SERPAPI_API_KEY or "
        "data/secrets/serpapi.env."
    )


def redact(value: object, key: str) -> object:
    if isinstance(value, dict):
        return {
            k: "[REDACTED]" if k.lower() == "api_key" else redact(v, key)
            for k, v in value.items()
        }
    if isinstance(value, list):
        return [redact(item, key) for item in value]
    if isinstance(value, str):
        return value.replace(key, "[REDACTED]")
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--departure", required=True)
    parser.add_argument("--arrival", required=True)
    parser.add_argument("--outbound", required=True)
    parser.add_argument("--return-date", required=True)
    parser.add_argument("--currency", default="EUR")
    parser.add_argument("--stops", choices=("0", "1", "2", "3"), default="1")
    parser.add_argument("--airlines")
    parser.add_argument("--departure-token")
    parser.add_argument("--deep-search", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    key = load_key()
    params = {
        "engine": "google_flights",
        "api_key": key,
        "departure_id": args.departure,
        "arrival_id": args.arrival,
        "outbound_date": args.outbound,
        "return_date": args.return_date,
        "type": "1",
        "currency": args.currency,
        "stops": args.stops,
        "output": "json",
    }
    if args.airlines:
        params["include_airlines"] = args.airlines
    if args.departure_token:
        params["departure_token"] = args.departure_token
    if args.deep_search:
        params["deep_search"] = "true"

    request = urllib.request.Request(
        "https://serpapi.com/search.json?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "surf-guide/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        print(f"SerpAPI HTTP error: {error.code}", file=sys.stderr)
        raise SystemExit(2) from None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"SerpAPI request failed: {type(error).__name__}", file=sys.stderr)
        raise SystemExit(2) from None

    json.dump(redact(payload, key), sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
