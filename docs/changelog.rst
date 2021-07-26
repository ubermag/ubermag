Changelog
=========

Upcoming version
----------------

New functionality
^^^^^^^^^^^^^^^^^

- Generalisation of OOMMF extensions `DMI_Cnv` and `DMI_D2d` to support grains oriented along `x`, `y`, or `z`
- Support for OOMMF extension `UHH_ThetaEvolve` for simulations at finite temperature. An example is given in the `oommfc` documentation.
- Support for arbitrary time-dependence for external magnetic fields (`mm.Zeeman`).

Bug fixes
^^^^^^^^^

- Multiple columns with the same name in `ubermagtable`.
- Removing a current term and driving the system caused a `TypeError`.
- `oommfc.compute` now works when current terms are specified in `system.dynamics`.

0.5.1
-----

- New subpackage `discretisedfield.tools` containing functions to operate on `discretisedfield.Field` objects
- New integration syntax
