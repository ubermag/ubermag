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
  - Fourier transform for ``discretisedfield.Field`` (`reference
    <https://ubermag.github.io/api/_autosummary/discretisedfield.Field.html#discretisedfield.Field.fftn>`__).
  - Custom labels for vector components in ``discretisedfield.Field``
    (`reference
    <https://ubermag.github.io/api/_autosummary/discretisedfield.Field.html#discretisedfield.Field.components>`__).
  - New plotting interface for ``discretisedfield.Field`` and
    ``discretisedfield.Region`` for both ``matplotlib`` and ``K3d``. Plotting
    functions can be accessed as ``Field.mpl.*`` (and for convenience
    ``Field.mpl()``) for ``matplotlib`` and similarly for ``K3d``.
  - Improved lightness plotting and new contour line plot.
  - Full support for complex values in ``discretisedfield.Field``.
  - Rotations of ``discretisedfield.Field`` objects (`documentation
    <https://ubermag.github.io/documentation/ipynb/discretisedfield/field-rotations.html>`__).
  - ``discretisedfield.Field`` now supports all ``numpy ufuncs``.
  - Calculation of the demag tensor and demag field in
    ``discretisedfield.tools`` (`reference
    <https://ubermag.github.io/api/_autosummary/discretisedfield.tools.demag_tensor.html>`__).

``mag2exp``
  - New subpackage ``mag2exp`` to simulate experimental measurement
    (`documentation <https://ubermag.github.io/documentation/mag2exp.html>`__).

``micromagneticmodel``
  - Generalisation of OOMMF extensions ``DMI_Cnv`` and ``DMI_D2d`` to support
    grains oriented along ``x``, ``y``, or ``z`` (new names, e.g. ``DMI_Cnv_z``)
    (`documentation
    <https://ubermag.github.io/documentation/ipynb/micromagneticmodel/energy-terms.html#5.-Dzyaloshinskii-Moriya-energy>`__).
  - Support for arbitrary time-dependence for external magnetic fields
    (``micromagneticmodel.Zeeman``) and spin-polarised currents
    (``micromagneticmodel.Slonczewski`` and ``micromagneticmodel.ZhangLi``).

``oommfc``
  - Support for OOMMF extension ``Xf_ThermHeunEvolver``,
    ``Xf_ThermSpinXferEvolver``, and ``UHH_ThetaEvolve`` for simulations at finite
    temperature.
  - Control over the default runner in ``oommfc`` via ``oommfc.runner`` object
    (`documentation
    <https://ubermag.github.io/documentation/ipynb/oommfc/controlling-default-runner.html>`__).

``ubermag``
  - Convenient control over logging of all subpackages via
    ``ubermag.setup_logging`` (`documentation <https://ubermag.github.io/documentation/ipynb/ubermag/logging.html>`__).

``ubermagtable``
  - Fourier transform for ``ubermagtable`` (`documentation
    <https://ubermag.github.io/documentation/ipynb/ubermagtable/table-fft.html>`__).

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
  - Removing a current term and driving the system caused a ``TypeError`` (`#135
    <https://github.com/ubermag/help/issues/135>`__).
  - ``oommfc.compute`` now works when current terms are specified in
    ``system.dynamics`` (`#139 <https://github.com/ubermag/help/issues/139>`__).
  - Wrong compute number in ``oommfc``.
  - ``oommfc`` is choosing the wrong runner when using ``pyenv`` (`#172
    <https://github.com/ubermag/help/issues/172>`__).

``ubermagtable``
  - Error in reading ODT files when using magnetoelastic extension (`#14
    <https://github.com/ubermag/ubermagtable/issues/14>`__).
  - Multiple columns with the same name in ``ubermagtable`` (`#118
    <https://github.com/ubermag/help/issues/118>`__).

0.51
====

- New subpackage ``discretisedfield.tools`` containing functions to operate on
  ``discretisedfield.Field`` objects.
- New integration syntax.
