=========
Changelog
=========

0.60.0
======

General
-------

- Unified website containing all documentation: https://ubermag.github.io
- Versions in sync across all packages
- Switch to Jupyter lab 3 (should improve situation with ``K3d`` inside Jupyter lab).

New functionality
-----------------

``discretisedfield``
  - Fourier transform for ``discretisedfield.Field``.
  - Custom labels for vector components in ``discretisedfield.Field``
  - New plotting interface for ``discretisedfield.Field`` and
    ``discretisedfield.Region`` for both ``matplotlib`` and ``K3d``. Plotting
    functions can be accessed as ``Field.mpl.*`` (and for convenience
    ``Field.mpl()``) for ``matplotlib`` and similarly for ``K3d``.
  - Improved lightness plotting and new contour line plot.
  - Full support for complex values in ``discretisedfield.Field``.
  - Rotations of ``discretisedfield.Field`` objects.
  - ``discretisedfield.Field`` now supports all ``numpy ufuncs``.
  - Calculation of the demag tensor and demag field in ``discretisedfield.tools``.

``mag2exp``
  - New subpackage ``mag2exp`` to simulate experimental measurement.

``micromagneticmodel``
  - Generalisation of OOMMF extensions ``DMI_Cnv`` and ``DMI_D2d`` to support
    grains oriented along ``x``, ``y``, or ``z`` (new names, e.g. ``DMI_Cnv_z``).
  - Support for arbitrary time-dependence for external magnetic fields
    (``micromagneticmodel.Zeeman``) and spin-polarised currents
    (``micromagneticmodel.Slonczewski`` and ``micromagneticmodel.ZhangLi``).

``oommfc``
  - Support for OOMMF extension ``Xf_ThermHeunEvolver``,
    ``Xf_ThermSpinXferEvolver``, and ``UHH_ThetaEvolve`` for simulations at finite
    temperature.
  - Control over the default runner in ``oommfc`` via ``oommfc.runner`` object.

``ubermag``
  - Convenient control over logging of all subpackages via
    ``ubermag.setup_logging``.

``ubermagtable``
  - Fourier transform for ``ubermagtable``.

Bug fixes
---------

``discretisedfield``
  - Wrong colourbar positioning in ``discretisedfield.mpl*`` in figures containing
    multiple subplots.
  - Fixed aspect ratio for ``quiver`` plots in ``discretisedfield.Field``.

``micromagneticmodel``
  - Creating a term ``micromagneticmodel.Slonczewski`` twice with the same
    dictionary for ``P`` or ``Lambda`` results in a ``ValueError``
``oommfc``
  - Removing a current term and driving the system caused a ``TypeError``.
  - ``oommfc.compute`` now works when current terms are specified in
    ``system.dynamics``.
  - Wrong compute number in ``oommfc``.
  - ``oommfc`` is choosing the wrong runner when using ``pyenv``.

``ubermagtable``
  - not properly reading ODT files when using magnetoelastic extension.
  - Multiple columns with the same name in ``ubermagtable``.

0.51
====

- New subpackage ``discretisedfield.tools`` containing functions to operate on
  ``discretisedfield.Field`` objects.
- New integration syntax.
