import pytest, json
from MainPackage.end_points import end_point_user
from MainPackage.test_common_operations import post, put_with_specification, get, delete
from MainPackage.baseUrlValidator import validate_url, base_url
from MainPackage.filename import payload

class TestUserClass:

    @pytest.mark.validate_baseurl
    def test_validate_baseurl(self, base_url):
        validate_url(base_url)
    @pytest.mark.post
    def test_post_request(self, base_url):
        post(base_url, end_point_user, payload("data_user"), "username")

    @pytest.mark.put
    def test_put_request(self, base_url):
        put_with_specification(base_url, end_point_user, payload("data_user"), payload("updated_user"), "username")

    @pytest.mark.get
    def test_get_request(self, base_url):
        get(base_url, end_point_user, payload("data_user"), "username")

    @pytest.mark.delete
    def test_delete_request(self, base_url):
        delete(base_url, end_point_user, payload("data_user"), "username")

    @pytest.mark.get
    def test_get_request(self, base_url):
        get(base_url, end_point_user, payload("data_user"), "username")