import ubermag


def test_version():
    assert isinstance(um.__version__, str)
    assert '.' in ubermag.__version__


def test_dependencies():
    assert isinstance(um.__dependencies__, list)
    assert len(ubermag.__dependencies__) > 0
