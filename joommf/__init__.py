import pkg_resources


def test():
    import pytest  # pragma: no cover
    return pytest.main(["-v", "--pyargs", "joommfutil"])  # pragma: no cover

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)
