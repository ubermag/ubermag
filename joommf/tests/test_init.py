import ubermag as um


def test_version():
    assert isinstance(um.__version__, str)
    assert '.' in um.__version__


def test_dependencies():
    assert isinstance(um.__dependencies__, list)
    assert len(um.__dependencies__) > 0
    
