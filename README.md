# Pyraminx Top First Helper

Pyraminx Top First Helper will find best starts with top-first methods.

## Demo
http://topfirst.ni-ken.net/

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

### Find best Bell start(s)
```
$ python3 findbell.py "U' L B U B L U B' l  b' "
L B' U' (B face)
```

### Find best 1-flip start(s)
```
$ python3 ./find1flip.py "L' B L' B L' R' U B L' R L l' b"
B U' R (U face)
```

## Find best intuitive starts(s)
```
$ python3 ./findintuitive.py "U' L B U R L u"
R B L R B (R face)
```

## Requirement
- Python 3
  - numpy
  - bottles (for demo)

## Author
Kentaro Nishi
(GitHub: [nikken7101](https://github.com/nikken7101)
WCA ID: [2006NISH01](https://www.worldcubeassociation.org/persons/2006NISH01),
Twitter: [@7y2n](https://twitter.com/7y2n))

## License
[MIT](https://github.com/nikken7101/pyraminx-top-first-helper/blob/master/LICENSE)
