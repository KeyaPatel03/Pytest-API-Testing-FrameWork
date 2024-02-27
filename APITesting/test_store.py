import pytest
from MainPackage.end_points import end_point_pet
from MainPackage.test_common_operations import post, get, delete
from MainPackage.baseUrlValidator import validate_url
from MainPackage.baseUrlValidator import base_url
from MainPackage.filename import payload

class TestStoreClass:

    @pytest.mark.validate_baseurl
    def test_validate_baseurl(self, base_url):
        validate_url(base_url)

    @pytest.mark.post
    def test_post_request(self, base_url):
        post(base_url, end_point_pet, payload("data_store"), "id")

    @pytest.mark.get
    def test_get_request(self, base_url):
        get(base_url, end_point_pet, payload("data_store"), "id")

    @pytest.mark.delete
    def test_delete_request(self, base_url):
        delete(base_url, end_point_pet, payload("data_store"), "id")

    @pytest.mark.get
    def test_get_request(self, base_url):
        get(base_url, end_point_pet, payload("data_store"), "id")

