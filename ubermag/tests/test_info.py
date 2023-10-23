import re

import ubermag


def test_debug_info():
    info = ubermag.debug_info()

    assert "Python: 3." in info

    for pkg in [
        "ubermagutil",
        "discretisedfield",
        "ubermagtable",
        "micromagneticmodel",
        "micromagneticdata",
        "micromagnetictests",
        "mumax3c",
        "oommfc",
        "mag2exp",
    ]:
        # test that all packages are listed with some version number
        assert re.findall(rf"{pkg}: [0-9.]+", info)

    assert f"ubermag: {ubermag.__version__}" in info

    # OOMMF is automatically installed so we can expect to find a Runner
    assert "OOMMFRunner" in info
