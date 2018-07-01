import joommf as jo

def test_version():
    assert isinstance(jo.__version__, str)
    assert '.' in jo.__version__

def test_dependencies():
    assert isinstance(jo.__dependencies__, list)
    assert len(jo.__dependencies__) > 0
    
