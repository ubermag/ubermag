import ubermag


def test_version():
    assert isinstance(ubermag.__version__, str)
    assert '.' in ubermag.__version__
