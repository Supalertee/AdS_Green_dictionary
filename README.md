# Green's Function Dictionary Package

This package is built to be the Python version of the Holographic mean-field theory, which is an extension part of our paper. <br />
**Mean field theory for strongly coupled systems: Holographic approach**: [ JHEP 06 (2024) 100](https://doi.org/10.1007/JHEP06%282024%29100)

The package contains Green's function and its physical quantity: Spectral function, 4x4 Green's function matrices, and their differentiation along momentum space.

# install

```zh
python -m pip install git+https://github.com/Supalertee/Green_dict.git#egg=Green_dict
```

# Using
```python
import Green_dict
```

# The package contains several contributions as following
1. spectral function generator <br />
  one can simply call the spectral function contribution as follows
```python
import Green_dict as Gd

Gd.spectra(Gd.<Interaction>, "<section>")

```
Where <Interaction> is a class of interaction which the user can select: 
| Class name      | Corresponding interaction |
| -------------   | ------------- |
| Noninteracting  | noninteracting system |
| Scalarss        | scalar SS quantization  |
| Scalarsa        | Scalar SA quantization  |
| Bxss            | vector Bx SS quantization |  
| Bxsa            | vector Bx SA quantization  |
| Bxyss           | tensor Bxy SS quantization |  
| Bxysa           | tensor Bxy SA quantization |
