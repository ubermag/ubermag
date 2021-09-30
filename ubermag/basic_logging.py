"""Setup basic logging for all ubermag packages."""
import logging


def setup_logging(level=logging.WARNING, package_levels=None):
    """Set up basic logging for Ubermag with per-package control.

    This function creates a basic logger (printing to stdout) and sets the log
    level for all packages in Ubermag to ``level``. Additional, more fine-grain
    control is possible by passing a dictionary to ``package_levels``. Keys
    must be ubermag subpackages, values log levels.

    Parameters
    ----------
    level : str, int, logging.LEVEL
        Log level used for all packages in Ubermag.

    package_levels : dict, optional
        Dictionary with Ubermag subpackage names as keys and log-levels
        as values. It allows fine-grain control over logging for
        individual packages.

    Example
    -------
    1. Setting up a basic logger with default log-level ``logging.WARNING``

    >>> import ubermag
    >>> ubermag.setup_logging()

    2. Setting up a basic logger with a higher log-level for ``oommfc``

    >>> import ubermag
    >>> ubermag.setup_logging(package_levels={'oommfc': logging.DEBUG})

    """
    # TODO Each package should use a single logger.
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

    # No change of the global log level to avoid logs from other packages
    # e.g. matplotlib
    # no fixed columns because (name) and (pathname) vary too much
    logging.basicConfig(format='%(asctime)s,%(msecs)d  %(name)s:%(levelname)s'
                        '  [%(pathname)s:%(funcName)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    package_levels = package_levels if package_levels is not None else {}

    for p in packages:
        logging.getLogger(p).setLevel(package_levels.get(p, level))
