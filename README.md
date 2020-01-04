# simpleWiener
A simple and fast implementation of Wiener's attack against small RSA exponent `d`

## Requirement
![shield](https://img.shields.io/badge/python-3.8.0%2B-blue)

## Usage
`cd` to the root of this repository and run the following in your terminal:
```
python3 -m simpleWiener.core e n
```
`e` and `n` are usually large integers you already know

## Example
```bash
python3 -m simpleWiener.core 9292162750094637473537 13029506445953503759481
```
output:
```
phi=13029506445724987531764
k=363
d=509
```

## Credits
https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf
https://github.com/orisano/owiener/blob/master/owiener.py

## License
MIT
