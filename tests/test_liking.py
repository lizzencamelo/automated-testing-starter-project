from src.liking.click_the_like_button import LikeState, click_many

def test_many_clicks():
    assert click_many(LikeState.empty, 'll') is LikeState.empty
    assert click_many(LikeState.empty, 'dd') is LikeState.empty
    assert click_many(LikeState.empty, 'ld') is LikeState.disliked
    assert click_many(LikeState.empty, 'dl') is LikeState.liked
    assert click_many(LikeState.empty, 'ldd') is LikeState.empty
    assert click_many(LikeState.empty, 'lldd') is LikeState.empty
    assert click_many(LikeState.empty, 'ddl') is LikeState.liked
    