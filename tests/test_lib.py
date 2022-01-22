from egoboostr719.lib import get_quote


def test_get_quote():
    assert len(get_quote()) > 0
    assert len(get_quote("Doug Berkley")) > 0
