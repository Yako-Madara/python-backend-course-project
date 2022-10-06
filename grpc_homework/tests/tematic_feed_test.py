import pytest
from tematic_feed.service import TematicFeedService
from tematic_feed.tematic_feed_pb2 import FeedRequest, PostCategory


@pytest.mark.parametrize("num_result, output", [(1, 1), (0, 0), (-3, 0), (40, 3)])
def test_feed_posts(num_result, output):
    service = TematicFeedService()
    request = FeedRequest(
        user_id=1, category=PostCategory.DEVELOPMENT, max_result=num_result
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == output
