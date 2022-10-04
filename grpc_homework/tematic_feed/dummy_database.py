from tematic_feed_pb2 import PostCategory, PostFeed

# Максимально игрушечная база данных
posts_by_category = {
    PostCategory.DEVELOPMENT: [
        PostFeed(id=1, title="The Maltese Falcon"),
        PostFeed(id=2, title="Murder on the Orient Express"),
        PostFeed(id=3, title="The Hound of the Baskervilles"),
    ],
    PostCategory.SCIENCE_FICTION: [
        PostFeed(id=4, title="The Hitchhiker's Guide to the Galaxy"),
        PostFeed(id=5, title="Ender's Game"),
        PostFeed(id=6, title="The Dune Chronicles"),
    ],
    PostCategory.TESTING: [
        PostFeed(id=7, title="The 7 Habits of Highly Effective People"),
        PostFeed(id=8, title="How to Win Friends and Influence People"),
        PostFeed(id=9, title="Man's Search for Meaning"),
    ],
}
