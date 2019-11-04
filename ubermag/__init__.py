import pytest
import pkg_resources

__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)


def test():
    """Runs tests for Ubermag and all its dependencies.

    The tests are going to be run for:
      - ubermagutil
      - discretisedfield
      - ubermagtable
      - micromagneticmodel
      - oommfc
      - ubermag

    """
    return pytest.main(['-m', 'not travis and not docker',
                        '-v', '--pyargs', 'ubermagutil',
                        'discretisedfield', 'ubermagtable',
                        'micromagneticmodel', 'oommfc',
                        'ubermag'])  # pragma: no cover
