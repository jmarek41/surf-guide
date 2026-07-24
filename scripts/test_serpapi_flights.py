from __future__ import annotations

import argparse
import io
import os
import unittest
from contextlib import redirect_stderr
from unittest import mock

import serpapi_flights


class SerpApiFlightsTests(unittest.TestCase):
    def test_load_key_reads_documented_env_file(self) -> None:
        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(serpapi_flights, "Path") as path_class,
        ):
            secret_file = path_class.return_value
            secret_file.exists.return_value = True
            secret_file.read_text.return_value = (
                "COMMENT=value\nSERPAPI_API_KEY=documented-key\n"
            )

            key = serpapi_flights.load_key()

        path_class.assert_called_once_with("data/secrets/serpapi.env")
        self.assertEqual(key, "documented-key")

    def test_redact_removes_key_from_nested_payload(self) -> None:
        key = "secret-value"
        payload = {
            "api_key": key,
            "nested": [{"url": f"https://example.test/?api_key={key}"}],
        }

        redacted = serpapi_flights.redact(payload, key)

        self.assertNotIn(key, repr(redacted))
        self.assertEqual(redacted["api_key"], "[REDACTED]")

    def test_top_level_api_error_exits_nonzero(self) -> None:
        args = argparse.Namespace(
            departure="PRG",
            arrival="LIS",
            outbound="2026-10-08",
            return_date="2026-10-11",
            currency="EUR",
            stops="1",
            airlines=None,
            departure_token=None,
            deep_search=False,
        )
        response = mock.MagicMock()
        response.__enter__.return_value = object()

        with (
            mock.patch.object(serpapi_flights, "parse_args", return_value=args),
            mock.patch.object(
                serpapi_flights, "load_key", return_value="secret-value"
            ),
            mock.patch.object(
                serpapi_flights.urllib.request, "urlopen", return_value=response
            ),
            mock.patch.object(
                serpapi_flights.json, "load", return_value={"error": "quota"}
            ),
            redirect_stderr(io.StringIO()) as stderr,
            self.assertRaises(SystemExit) as raised,
        ):
            serpapi_flights.main()

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("request was rejected", stderr.getvalue())
        self.assertNotIn("secret-value", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
