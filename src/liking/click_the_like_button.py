import enum

class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


click_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

click_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def click_like(s: LikeState) -> LikeState:
    return click_like_transitions[s]


def click_dislike(s: LikeState) -> LikeState:
    return click_dislike_transitions[s]


def click_many(s: LikeState, clicks: str) -> LikeState:
    for c in clicks:
        c = c.lower()
        if c == 'l':
            s = click_like(s)
        elif c == 'd':
            s = click_dislike(s)
        else:
            raise ValueError('invalid click')
    return s
