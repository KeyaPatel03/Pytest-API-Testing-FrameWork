import pytest, json
from MainPackage.end_points import end_point_pet
from MainPackage.test_common_operations import post, put, get, delete
from MainPackage.baseUrlValidator import validate_url
from MainPackage.baseUrlValidator import base_url

class TestPetClass:
    @pytest.fixture
    def payload(self):
        with open('..\\TestData\\data_pet.json.json', 'r') as file:
            data = json.load(file)
            return data

    @pytest.fixture
    def updated_payload(self):
        with open('..\\TestData\\updated_pet.json', 'r') as file:
            u_data = json.load(file)
            return u_data

    @pytest.fixture
    def test_validate_baseurl(self, base_url):
        validate_url(base_url)

    @pytest.mark.post
    def test_post_request(self, base_url, payload):
        post(base_url, end_point_pet, payload, "id")

    @pytest.mark.put
    def test_put_request(self, base_url, payload, updated_payload):
        put(base_url, end_point_pet, payload, updated_payload)

    @pytest.mark.get
    def test_get_request(self, base_url, payload):
        get(base_url, end_point_pet, payload, "id")

    @pytest.mark.delete
    def test_delete_request(self, base_url, payload):
        delete(base_url, end_point_pet, payload, "id")

    @pytest.mark.get
    def test_get_request(self, base_url, payload):
        get(base_url, end_point_pet, payload, "id")