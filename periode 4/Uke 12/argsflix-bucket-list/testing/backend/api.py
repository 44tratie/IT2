from backend.api import APIWrapper


def test_api():
    api = APIWrapper()

    # test query
    query_result = api.query_movie("avatar")

    # test id lookup
    lookup_result = api.by_id(query_result[0].imdb_id)

    # check if results match
    assert lookup_result.title == query_result[0].title
    assert lookup_result.year == query_result[0].year
    assert lookup_result.imdb_id == query_result[0].imdb_id
    assert lookup_result.type_ == query_result[0].type_
    assert lookup_result.poster == query_result[0].poster
