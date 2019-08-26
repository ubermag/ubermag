import pytest
import pkg_resources

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)


def test():
    return pytest.main(['-m', 'not travis and not docker',
                        '-v', '--pyargs', 'ubermagutil',
                        'discretisedfield', 'ubermagtable',
                        'micromagneticmodel', 'oommfc',
                        'ubermag'])  # pragma: no cover
