import pytest
import pkg_resources


def test():
    return pytest.main(["-v", "--pyargs", "joommfutil",
                        #"discretisedfield",
                        "oommfodt",
                        "micromagneticmodel", "oommfc",
                        "joommf"])  # pragma: no cover

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)
