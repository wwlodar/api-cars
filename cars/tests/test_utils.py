from rest_framework.test import APIRequestFactory, APITestCase
from ..utils import get_data
import mock 

class MockResponseSuccess:

    def __init__(self):
        self.status_code = 200

    def json(self):
        return {"Count": 14, "Message": "Response returned successfully", "SearchCriteria": "Make:Fiat", 
        "Results": [{"Make_ID": 492, "Make_Name": "FIAT", "Model_ID": 3490, "Model_Name": "Freemont"}]}

class MockResponseFail:

    def __init__(self):
        self.status_code = 404

    def json(self):
        return {"Count": 0, "Message": "Response returned successfully", "SearchCriteria": "Make:fiatl", "Results": []}

class TestGetData(APITestCase):
    @mock.patch("requests.get", return_value=MockResponseSuccess())
    def test_get_correct_name(self, mock_result):
        make = 'Fiat'
        result = get_data(make=make)

        self. assertEqual(result, [{'Make_ID': 492, 'Make_Name': 'FIAT', 'Model_ID': 3490, 'Model_Name': 'Freemont'}])

    @mock.patch("requests.get", return_value=MockResponseFail())
    def test_404_response(self, mock_result):
        make = 'Fiat'
        result = get_data(make=make)

        self. assertEqual(result, [])
