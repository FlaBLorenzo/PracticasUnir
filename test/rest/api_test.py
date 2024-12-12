import unittest
from urllib.request import urlopen
from urllib.error import URLError
import http.client

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

class TestApi(unittest.TestCase):

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode().strip(), '{"result": 3}', "ERROR ADD")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode().strip(), '{"result": 5.0}', "ERROR DIVIDE")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except URLError as e:
            self.assertEqual(e.code, 406, "Expected HTTP 406 for division by zero")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode().strip(), '{"result": 12}', "ERROR MULTIPLY")

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/subtract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode().strip(), '{"result": 2}', "ERROR SUBTRACT")

if __name__ == "__main__":
    unittest.main()



