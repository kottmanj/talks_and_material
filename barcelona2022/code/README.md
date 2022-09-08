# Code examples from Barcelone talk
- see slides for filenames
## Install tequila
```bash
pip install tequila-basic
```
Also recommended: install a fast simulator (will be used automatically)
```bash
pip install qulacs
```

## Install Chemistry Backends
### pyscf needed for most code examples
```bash
pip install pyscf
```
### madness backend (orbital-free approaches from the automatization section)  
- will only work for Linux-64 (see tequila-github for more information on other systems)  
- only needed for some code examples
```bash
conda install madtequila -n kottmann
```
