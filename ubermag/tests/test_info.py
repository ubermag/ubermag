import re

import mumax3c

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


def test_debug_info_runner_without_version(monkeypatch):
    # mumax3c runners have no ``version`` attribute; debug_info must not fail
    monkeypatch.setattr(mumax3c.runner, "cache_runner", True)
    monkeypatch.setattr(mumax3c.runner, "_runner", mumax3c.mumax3.ExeMumax3Runner())
    info = ubermag.debug_info()
    assert "Mumax3: " in info
    assert "ExeMumax3Runner" in info
