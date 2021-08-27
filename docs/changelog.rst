=========
Changelog
=========

Upcoming version
================

General
-------
- Unified website containing all documentation: https://ubermag.github.io
- Versions in sync across all packages

New functionality
-----------------

- Generalisation of OOMMF extensions ``DMI_Cnv`` and ``DMI_D2d`` to support grains oriented along ``x``, ``y``, or ``z``
- Support for OOMMF extension ``UHH_ThetaEvolve`` for simulations at finite temperature. An example is given in the ``oommfc`` documentation.
- Support for arbitrary time-dependence for external magnetic fields (``mm.Zeeman``).
- Fourier transform for ``discretisedfield.Field``.
- New plotting interface for ``discretisedfield.Field`` and ``discretisedfield.Region``.
- Support for complex fields.
- Control over the default runner in ``oommfc`` via ``oommfc.runner`` object.
- Convenient control over logging of all subpackages via ``ubermag.setup_logging``.

TODO / in progress
- New subpackages ``mag2exp`` to simulate experimental measurements.
- Rotations of the field object
- simplified integral syntax

Bug fixes
---------

- Multiple columns with the same name in ``ubermagtable``.
- Removing a current term and driving the system caused a ``TypeError``.
- ``oommfc.compute`` now works when current terms are specified in ``system.dynamics``.
- Wrong colourbar positioning in ``discretisedfield.mpl*`` in figures containing multiple subplots.

0.5.1
=====

- New subpackage ``discretisedfield.tools`` containing functions to operate on ``discretisedfield.Field`` objects
- New integration syntax
