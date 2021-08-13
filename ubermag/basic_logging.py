"""Setup basic logging for all ubermag packages."""
import logging


def setup_logging(level=logging.WARNING, package_levels=None):
    """Set up basic logging for Ubermag with per-package control.

    This function creates a basic logger (printing to stdout) and sets the log
    level for all packages in ubermag to ``level``. Additional, more fine-grain
    control is possible by passing a dictionary to ``package_levels``. Keys
    must be ubermag subpackages, values log levels.

    Parameters
    ----------
    level : str, int, logging.LEVEL
        Log level used for all packages in ubermag.

    package_levels : dict, optional Dictionary with ubermag subpackage names as
        keys and log-levels as values. Allows fine-grain control over logging
        for individual packages.

    Example
    -------
    1. Setting up a basic logger with default log-level ``logging.WARNING``

    >>> import ubermag
    >>> ubermag.setup_logging()

    2. Setting up a basic logger with a higher log-level for ``oommfc``

    >>> import ubermag
    >>> ubermag.setup_logging(package_levels={'oommfc': logging.DEBUG})

    """
    # TODO Each packages should use a single logger.
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

    # TODO Use better configuration, e.g.:
    # <LEVEL>: <package>/<file>/line <line-number>: <msg>

    # No change of the global log level to avoid logs from other packages
    # such as matplotlib
    logging.basicConfig()

    if package_levels is not None:
        for p in package_levels.keys():
            logging.getLogger(p).setLevel(package_levels.get(p, level))
    else:
        for p in packages:
            logging.getLogger(p).setLevel(level)
