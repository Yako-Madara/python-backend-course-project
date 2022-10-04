import random

import grpc
import tematic_feed_pb2_grpc
from dummy_database import posts_by_category
from tematic_feed_pb2 import FeedResponse


class TematicFeedService(tematic_feed_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in posts_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        posts_for_category = posts_by_category[request.category]
        num_results = max(min(request.max_results, len(posts_for_category)))
        posts_to_feed = random.sample(posts_for_category, num_results)

        return FeedResponse(recommendations=posts_to_feed)
