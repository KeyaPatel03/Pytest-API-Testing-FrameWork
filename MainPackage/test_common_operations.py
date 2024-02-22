import requests, pytest
import logging
from MainPackage.end_points import end_point_request
from MainPackage.baseUrlValidator import base_url
logger = logging.getLogger()

# e_response = {"key": "value"}
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
        # raise Exception (f"\nPOST request failed. Error: {e}")
        logger.error(f"\n\nPOST request failed. Error: {e}")
        return False

@pytest.mark.get
def get(base_url, endpoint, data, key):
    try:
        global e_response
        response = requests.get(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
        response.raise_for_status()
        print("\n\nGET request successful.\nResponse:", response.json())
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nGET request failed. Error: {e}")
        return False

@pytest.mark.put
def put(base_url, endpoint, data, udata):
    try:
        response = requests.put(f'{base_url}{endpoint}', json=udata)
        response.raise_for_status()
        print("\n\nPUT request successful.\nResponse:", response.json())
        for key in data:
            if data[key] != udata[key]:
                print(f"{key} FAIL {data[key]}")
            else:
                print(f"{key} PASS {data[key]}")
                # sys.exit()
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nPUT request failed. Error: {e}")
        return False

@pytest.mark.put_specification
def put_with_specification(base_url, endpoint, data, udata, key):
    try:
        global e_response
        print(e_response)
        response = requests.put(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=udata)
        print("\n\nPUT request successful.\nResponse:", response.json())
        for key in data:
            if data[key] != udata[key]:
                print(f"{key} FAIL {data[key]}")
            else:
                print(f"{key} PASS {data[key]}")
                # sys.exit()
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nPUT request failed. Error: {e}")
        return False

@pytest.mark.delete
def delete(base_url, endpoint, data, key):
    try:
        response = requests.delete(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
        print("\n\nDELETE request successful.\nResponse:", response.json())
        response.raise_for_status()
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"\n\nDELETE request failed. Error: {e}")
        return False


