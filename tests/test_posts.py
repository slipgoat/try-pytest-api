from assertpy import assert_that

from core.clients.api.api_client import ApiClient


class TestPosts:

    def test_post_list(self, api_client: ApiClient):
        posts = api_client.get_posts()
        assert_that(len(posts)).is_greater_than(0)
        assert_that(posts[0].id).is_instance_of(int)

    def test_post_detail(self, api_client):
        post = api_client.get_post(1)
        assert_that(post.id).is_equal_to(1)
        assert_that(post.title).is_not_none()
        assert_that(post.body).is_not_none()
        assert_that(post.userId).is_not_none()
