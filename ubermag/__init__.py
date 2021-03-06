"""Main package"""
import pytest
import pkg_resources

__version__ = pkg_resources.get_distribution(__name__).version


def test():
    """Run all package tests.

    Examples
    --------
    1. Run all tests.

    >>> import ubermag
    ...
    >>> # ubermag.test()

    """
    return pytest.main(['-m', 'not travis and not docker',
                        '-v', '--pyargs', 'ubermagutil', 'discretisedfield',
                        'ubermagtable', 'micromagneticmodel', 'oommfc',
                        'micromagnetictests', 'micromagneticdata',
                        'ubermag', '-l'])  # pragma: no cover
