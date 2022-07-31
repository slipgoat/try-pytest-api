from functools import partial
from typing import Optional, Callable, Any, Union, TypeVar, Type
from urllib.parse import urljoin
from pydantic import BaseModel as PydanticBaseModel

from requests import Session, Response as RequestsResponse

from core.models.base_model import BaseModel


class Request(BaseModel):
    method: str
    path: str
    response_code: Optional[int]
    parser: Optional[Callable]
    headers: Optional[str]


class Response(BaseModel):
    status_code: int
    headers: Any
    body: Any


Handler = Callable[[Request], RequestsResponse]
Middleware = Callable[[Handler, Request], Response]
T = TypeVar("T", bound=PydanticBaseModel)


class BaseApiClient(Session):
    def __init__(self, base_path: str, token: str = None, middlewares: list[Middleware] = None):
        super(BaseApiClient, self).__init__()
        self.base_path = base_path
        self.token = token
        self.middlewares = [] if middlewares is None else middlewares

    def fetch(self, request: Request) -> Union[Type[T], dict, str]:
        if self.token:
            self.headers.update({'Authorization': f'Bearer: {self.token}'})

        request_updated = request.copy()
        request_updated.headers = self.headers
        handler = self._execute

        for middleware in self.middlewares:
            handler = partial(middleware, handler)
        response = handler(request_updated)
        return request.parser(response.json()) if request.parser is not None else response.json()

    def _execute(self, request: Request) -> RequestsResponse:
        url = urljoin(self.base_path, request.path)
        response = super(BaseApiClient, self).request(request.method, url)

        if request.response_code is not None:
            assert response.status_code == request.response_code

        return response
