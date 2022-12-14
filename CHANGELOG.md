# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Changed
 - Tune `is_bright` to a more acceptable value


## [0.1.4] — 2022-08-21
### Fixed
 - Fix red/green color components returning incorrect values (this led to `hsv`, `is_greyscale`, `perceived_brightness`, and all other derivative properties being incorrect...)
 - Resolve `NameError` in `as_srgb_color` and `as_lab_color` when colormath _was_ installed


## [0.1.3] — 2022-08-20
### Fixed
 - Resolve `ImportError` when colormath not installed


## [0.1.2] — 2022-08-19
### Changed
 - Improve display of background color swatches

### Fixed
 - Resolve incorrect typing for color members on Fore256/Back256


## [0.1.1] — 2022-08-18
### Changed
 - Include license and changelog in source distribution


## [0.1.0] — 2022-08-18
### Added
 - Added `Fore256` and `Back256` classes for controlling foreground/background color
 - Added utilities for printing colours in various formats
 - Added utilities for automatically finding differentiated colours
