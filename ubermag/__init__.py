"""Meta package for the Ubermag project."""
import importlib.metadata

import pytest

from .info import debug_info

__version__ = importlib.metadata.version(__package__)


def test():
    """Run all package tests.

    Examples
    --------
    1. Run all tests.

    >>> import ubermag
    ...
    >>> # ubermag.test()

    """
    return pytest.main(
        [
            "-m",
            "not travis and not docker",
            "-v",
            "--pyargs",
            "ubermagutil",
            "discretisedfield",
            "ubermagtable",
            "micromagneticmodel",
            "oommfc",
            "micromagnetictests",
            "micromagneticdata",
            "mag2exp",
            # "mumax3c",  # mumax3 is not necessarily available -> no tests
            "ubermag",
            "-l",
        ]
    )  # pragma: no cover
