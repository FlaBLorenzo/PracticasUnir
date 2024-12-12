import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import http.client
import json

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

class TestApi(unittest.TestCase):

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
            result = json.loads(response.read().decode().strip())
            self.assertEqual(result, {"result": 3}, "ERROR ADD")
        except HTTPError as e:
            self.fail(f"HTTPError: {e}")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
            result = json.loads(response.read().decode().strip())
            self.assertEqual(result, {"result": 5.0}, "ERROR DIVIDE")
        except HTTPError as e:
            self.fail(f"HTTPError: {e}")


    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
            result = json.loads(response.read().decode().strip())
            self.assertEqual(result, {"result": 12}, "ERROR MULTIPLY")
        except HTTPError as e:
            self.fail(f"HTTPError: {e}")

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/subtract/5/3"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
            result = json.loads(response.read().decode().strip())
            self.assertEqual(result, {"result": 2}, "ERROR SUBTRACT")
        except HTTPError as e:
            self.fail(f"HTTPError: {e}")

if __name__ == '__main__':
    unittest.main()





