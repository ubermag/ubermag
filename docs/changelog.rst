=========
Changelog
=========

0.60.0
======

General
-------

- Unified website containing all documentation: https://ubermag.github.io
- Versions in sync across all packages

New functionality
-----------------

- Fourier transform for ``discretisedfield.Field``.
- New plotting interface for ``discretisedfield.Field`` and
  ``discretisedfield.Region``.
- Full support for complex values in ``discretisedfield.Field``.
- Rotations of ``discretisedfield.Field`` objects.
- Generalisation of OOMMF extensions ``DMI_Cnv`` and ``DMI_D2d`` to support
  grains oriented along ``x``, ``y``, or ``z`` (new names, e.g. ``DMI_Cnv_z``).
- Support for arbitrary time-dependence for external magnetic fields
  (``micromagneticmodel.Zeeman``) and spin-polarised currents
  (``micromagneticmodel.Slonczewski`` and ``micromagneticmodel.ZhangLi``).
- Support for OOMMF extension ``Xf_ThermHeunEvolver``,
  ``Xf_ThermSpinXferEvolver``, and ``UHH_ThetaEvolve`` for simulations at finite
  temperature.
- Control over the default runner in ``oommfc`` via ``oommfc.runner`` object.
- Convenient control over logging of all subpackages via
  ``ubermag.setup_logging``.
- New subpackage ``mag2exp`` to simulate experimental measurements.

Bug fixes
---------

- Multiple columns with the same name in ``ubermagtable``.
- Removing a current term and driving the system caused a ``TypeError``.
- ``oommfc.compute`` now works when current terms are specified in
  ``system.dynamics``.
- Wrong colourbar positioning in ``discretisedfield.mpl*`` in figures containing
  multiple subplots.
- Wrong compute number in ``oommfc``.

0.51
====

- New subpackage ``discretisedfield.tools`` containing functions to operate on
  ``discretisedfield.Field`` objects.
- New integration syntax.
