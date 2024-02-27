import requests, pytest, sys
import logging
from MainPackage.end_points import end_point_request
from MainPackage.baseUrlValidator import base_url
logger = logging.getLogger()

e_response = {"key": "value"}
@pytest.mark.post
def post(base_url, endpoint, data, key):
    try:
        global e_response
        response_post = requests.post(f'{base_url}{endpoint}', json=data)
        e_response = response_post.json()
        print("\n\nPOST request successful.\nResponse:", e_response)
        print("Print ID:", end_point_request(data, key, e_response))
        return e_response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nPOST request failed. Error: {e}")
        sys.exit()

@pytest.mark.get
def get(base_url, endpoint, data, key):
    try:
        global e_response
        response = requests.get(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
        print("\n\nGET request successful.\nResponse:", response.json())
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nGET request failed. Error: {e}")
        sys.exit()

@pytest.mark.put
def put(base_url, endpoint, data, udata):
    try:
        global e_response
        response = requests.put(f'{base_url}{endpoint}', json=udata)
        e_response = response.json()
        print("\n\nPUT request successful.\nResponse:", response.json())
        for key in data:
            if data[key] == udata[key]:
                print(f"{key} FAIL")
            else:
                print(f"{key} PASS")

        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nPUT request failed. Error: {e}")
        sys.exit()

@pytest.mark.put_specification
def put_with_specification(base_url, endpoint, data, udata, key):
    try:
        global e_response
        print(e_response)
        response = requests.put(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=udata)
        print("\n\nPUT request successful.\nResponse:", response.json())
        for key in data:
            if data[key] != udata[key]:
                print(f"{key} FAIL")
            else:
                print(f"{key} PASS")
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nPUT request failed. Error: {e}")
        sys.exit()

@pytest.mark.delete
def delete(base_url, endpoint, data, key):
    try:
        global e_response
        response = requests.delete(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
        print("\n\nDELETE request successful.\nResponse:", response.json())
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nDELETE request failed. Error: {e}")
        sys.exit()

