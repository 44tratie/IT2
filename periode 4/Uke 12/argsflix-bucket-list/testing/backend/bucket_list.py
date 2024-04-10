from backend.api import APIWrapper
from backend.bucket_list import BucketList


def test_bucket_list():
    bucket_list = BucketList()

    # reset the list
    bucket_list.reset_list()

    assert not bucket_list.list
    assert not bucket_list.seen

    # get an api to query a movie
    api = APIWrapper()
    query_res = api.query_movie("avatar")

    test_id = query_res[0].imdb_id

    # add movie to list
    bucket_list.add_to_list(query_res[0])

    assert test_id in bucket_list.list
    assert test_id not in bucket_list.seen

    # mark movie as seen
    bucket_list.update_seen(test_id)

    assert test_id in bucket_list.seen

    # unsee movie
    bucket_list.update_seen(test_id)

    assert test_id not in bucket_list.seen

    # remove movie from list
    bucket_list.remove_from_list(test_id)

    assert test_id not in bucket_list.list
