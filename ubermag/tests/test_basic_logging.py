import ubermag
import logging


def check_levels(level=logging.WARNING, per_package=None):
    packages = [
        'discretisedfield',
        'mag2exp',
        'micromagneticdata',
        'micromagneticmodel',
        'micromagnetictests',
        'oommfc',
        'ubermagtable',
        'ubermagutil',
    ]

    # Root log level should not be modified
    assert logging.getLogger('').level == 30

    for p in packages:
        if per_package is None:
            assert logging.getLogger(p).level == level
        else:
            assert logging.getLogger(p).level == per_package.get(p, level)


def test_setup_logging_default():
    ubermag.setup_logging()
    check_levels()


def test_setup_logging_levels():
    for level in [10, "DEBUG", logging.DEBUG]:
        ubermag.setup_logging(level)
        check_levels(logging.DEBUG)


def test_setup_logging_per_package():
    package_levels = {
        'discretisedfield': 0,
        'mag2exp': 10,
        'micromagneticdata': 20,
        'micromagneticmodel': 30,
        'micomagnetictests': 40,
        'oommfc': 50,
    }
    ubermag.setup_logging(level=logging.INFO, package_levels=package_levels)
    check_levels(logging.INFO, package_levels)
