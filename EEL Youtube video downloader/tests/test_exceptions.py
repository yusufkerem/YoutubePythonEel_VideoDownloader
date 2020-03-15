# -*- coding: utf-8 -*-
from pytube.exceptions import VideoUnavailable, RegexMatchError, LiveStreamError


def test_video_unavailable():
    try:
        raise VideoUnavailable(video_id="YLnZklYFe7E")
    except VideoUnavailable as e:
        assert e.video_id == "YLnZklYFe7E"
        assert str(e) == "YLnZklYFe7E is unavailable"


def test_regex_match_error():
    try:
        raise RegexMatchError(caller="hello", pattern="*")
    except RegexMatchError as e:
        assert str(e) == "hello: could not find match for *"


def test_live_stream_error():
    try:
        raise LiveStreamError(video_id="YLnZklYFe7E")
    except LiveStreamError as e:
        assert e.video_id == "YLnZklYFe7E"
        assert str(e) == "YLnZklYFe7E is streaming live and cannot be loaded"
