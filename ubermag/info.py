import importlib
import sys


def debug_info():
    """Collect inforamtion about ubermag subpackages and available calculators."""
    info_str = f"Platform: {sys.platform}\nPython: {sys.version}\n\n"

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
        "ubermag",
    ]:
        module = importlib.import_module(pkg)
        version = getattr(module, "__version__")
        info_str += f"{pkg}: {version}\n"

    info_str += "\n"

    for pkg, calculator in [("oommfc", "OOMMF"), ("mumax3c", "Mumax3")]:
        try:
            module = importlib.import_module(pkg)
            runner = getattr(module, "runner").__getattribute__("runner")
        except OSError as e:
            info_str += f"{calculator}: {e}\n"
        else:
            info_str += f"{calculator}: {runner}, {runner.version}\n"

    return info_str
