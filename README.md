# simpleWiener
A simple and fast implementation of Wiener's attack against small RSA exponent `d`

## Requirement
Python 3.8.0+

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

## License
MIT