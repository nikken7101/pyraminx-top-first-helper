# Pyraminx-top-first-helper

Pyraminx-top-first-helper will find best starts with Oka method and Keyhole method.

## Usage
### Find best Oka start(s)
```
$ python3 findoka.py "R U' R' U R' U R' L' R L' U u' l r b"
U' L' R (U face)
L' U' R (U face)
U' L' U' R (B face)
L' R' U R' (U face)
```

### Find best Keyhole start(s)
```
$ python3 findkeyhole.py "U' B' R U' B U' B R' U' R U' u' l' r'"
U' R' (B face)
```

## Requirement
- Python 3
  - numpy
  - bottles (for demo)

## Author
Kentaro Nishi (WCA ID: [2006NISH01](https://www.worldcubeassociation.org/persons/2006NISH01))

## License
[MIT](https://github.com/nikken7101/pyraminx-top-first-helper/blob/master/LICENSE)
