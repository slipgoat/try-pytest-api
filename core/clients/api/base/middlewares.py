import json
import logging

from requests import Response

from core.clients.api.base.base_api_client import Request, Handler


def log_api(handler: Handler, request: Request) -> Response:
    response = handler(request)
    logging.debug(f"Request Headers\n{request.headers}")
    logging.debug(f"Response Headers\n{response.headers}")
    logging.debug(f"Response Body\n{json.dumps(response.json(), indent=2)}")
    return response
