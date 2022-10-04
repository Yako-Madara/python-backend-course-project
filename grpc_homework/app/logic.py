import os

import grpc
from flask import render_template
from tematic_feed_pb2 import FeedRequest, PostCategory
from tematic_feed_pb2_grpc import RecommendationsStub

tematic_feed_host = os.getenv("TEMATIC_FEED_HOST", "localhost")
tematic_feed_channel = grpc.insecure_channel(f"{tematic_feed_host}:50051")
tematic_feed_client = RecommendationsStub(tematic_feed_channel)

categories = {
    "development": PostCategory.DEVELOPMENT,
    "sciense_fiction": PostCategory.SCIENCE_FICTION,
    "testing": PostCategory.TESTING,
}


def get_feed_for_category(category: str):
    """Возвращает страницу с тематическими постами.

    Args:
        category (str): тематика статей

    Returns: страница с постами на определенную тему
    """
    post_category = categories[category]
    request = FeedRequest(user_id=1, category=post_category, max_result=3)
    posts_for_feed_response = tematic_feed_client.Recommend(request)
    return render_template(
        "feedpage.html",
        posts_for_feed=posts_for_feed_response.recommendations,
    )
