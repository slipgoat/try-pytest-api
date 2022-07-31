from core.clients.api.base.base_api_client import BaseApiClient, Request
from core.clients.api.base.middlewares import log_api
from core.models.post import Post


class ApiClient(BaseApiClient):
    
    def __init__(self, token: str = None):
        super(ApiClient, self).__init__(
            base_path="https://jsonplaceholder.typicode.com/",
            token=token,
            middlewares=[log_api]
        )
    
    def get_posts(self) -> list[Post]:
        request = Request(
            method="GET",
            path="posts",
            response_code=200,
            parser=lambda posts: [Post.from_dict(post) for post in posts]
        )
        return self.fetch(request)

    def get_post(self, post_id: int) -> Post:
        request = Request(
            method="GET",
            path=f"posts/{post_id}",
            response_code=200,
            parser=Post.from_dict
        )
        return self.fetch(request)
