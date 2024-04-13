import requests
from yandex_tracker_client import TrackerClient
from http import HTTPStatus
from loguru import logger


def check_token(token: str, org_id: str) -> bool:
    session = requests.Session()
    head = {
        "Authorization": f"OAuth {token}",
        "X-Cloud-Org-ID": org_id
    }
    session.headers.update(head)
    response = session.get("https://api.tracker.yandex.net/v2/myself")
    if not response.status_code == HTTPStatus.OK:
        logger.error("Token is not valid")
        return False
    logger.error("Token is valid")
    return True


def get_tracker_client(token: str, org_id: str) -> TrackerClient:
    if not check_token(token, org_id):
        raise Exception

    client = TrackerClient(token=token, cloud_org_id=org_id)
    return client
