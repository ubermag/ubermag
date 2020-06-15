import pytest
import pkg_resources


def test():
    return pytest.main(['-m', 'not travis and not docker',
                        '-v', '--pyargs', 'ubermagutil', 'discretisedfield',
                        'ubermagtable', 'micromagneticmodel', 'oommfc',
                        'micromagnetictests', 'micromagneticdata',
                        'ubermag'])  # pragma: no cover


__version__ = pkg_resources.get_distribution(__name__).version
__dependencies__ = pkg_resources.require(__name__)
