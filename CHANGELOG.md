# Release Note

## Pending
### Add
 - new data source Sec.or.th

## 0.4.0 - 5 June 2026
### Fixed
 - `get()` works again: Finnomena retired the `nav/latest` endpoint, so the
   latest NAV is now derived from the v2 range endpoint
 - `import pythainav` works on Python 3.12+ (dropped removed `distutils`)
 - add the missing `base64` import used by the Sec factsheet helpers

### Changed
 - `get()` now pulls full history so latest and historical `date` lookups
   resolve regardless of how old the fund's most recent NAV is
 - require Python >= 3.9 (drop end-of-life 3.7 / 3.8); modern type hints
 - drop the GPL-licensed `fuzzywuzzy` dependency (MIT compliance)
 - migrate tooling to uv + mise + hk + ruff; CI tested on Python 3.9–3.13

## 0.1.5 - 9 March 2020

### Fixes
 - down pandas min version to 0.25.3 for google colab support

## 0.1.5 - 9 March 2020

### Added
 - get() now support date parameter
 - add get_all()
 - update docs, readme, source of data

## 0.1.3 - 25 Jan 2020

### Fixes
 - dataclasses error on python 3.6

## 0.1.2 - 25 Jan 2020

### Features

 - Change to api call = more lightweight + faster

### Fixes
 - Add compatibility to python 3.6

## 0.1.1 - 24 Jan 2020

### Misc.
 - Setup skeleton for future development
 - Refactor the code
