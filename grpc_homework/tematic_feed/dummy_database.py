from tematic_feed_pb2 import PostCategory, PostFeed

# Максимально игрушечная база данных
posts_by_category = {
    PostCategory.DEVELOPMENT: [
        PostFeed(id=1, title="Ускоряем разработку в VSCode"),
        PostFeed(
            id=2, title="Интересное о протоколах, сетях и работе интернет-провайдеров"
        ),
        PostFeed(id=3, title="Linux Kernel 6.0: что нового «выросло» в ядре?"),
    ],
    PostCategory.SCIENCE_FICTION: [
        PostFeed(id=4, title="Cнова про llvm"),
        PostFeed(id=5, title="Как включить журналы базы данных"),
        PostFeed(id=6, title="Особенности реализации List в C#"),
    ],
    PostCategory.TESTING: [
        PostFeed(
            id=7, title="GeekUniversity открывает набор на факультет тестирования ПО"
        ),
        PostFeed(
            id=8, title="Яндекс Практикум запускает курс «Инженер по тестированию плюс»"
        ),
        PostFeed(id=9, title="Что такое тестирование?"),
    ],
}
