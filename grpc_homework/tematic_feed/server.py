from concurrent import futures

import grpc
import tematic_feed_pb2_grpc
from service import TematicFeedService


def server():
    """Функция, запускающая сетевой grpc сервер."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tematic_feed_pb2_grpc.add_RecommendationsServicer_to_server(
        TematicFeedService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
