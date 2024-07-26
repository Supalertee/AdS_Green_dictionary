# Green's Function Dictionary Package

This package is built to be the Python version of the Holographic mean-field theory, which is an extension part of our paper. <br />
**Mean field theory for strongly coupled systems: Holographic approach**: [ JHEP 06 (2024) 100](https://doi.org/10.1007/JHEP06%282024%29100)

The package contains Green's function and its physical quantity: Spectral function, 4x4 Green's function matrices, and their differentiation along momentum space.

# installation

```zh
python -m pip install git+https://github.com/Supalertee/Green_dict.git#egg=Green_dict
```

# Using
```python
import Green_dict
```

# The package contains several contributions as following
1. **Spectral Density Generator** <br />
  one can simply call the spectral function contribution as follows
```python
import Green_dict as Gd

Gd.spectra(Gd.<Interaction>)##, section = "all"  , kx =0 ,ky=0,kz=0,omega =0  by default##)

```
Mathematically, the "Interaction" is defined from interacting lagrangian as follows
```math
\mathcal{L}_{int} = \bar\psi^{(2)}\Gamma \cdot \Phi \psi^{(1)} + h.c. where
```
```math
\Gamma \cdot \Phi = i I \Phi \quad\text{scalar cases} \quad\quad
\Gamma \cdot \Phi = \Gamma^\mu B_\mu \quad\text{vector cases}\quad\quad
\Gamma \cdot \Phi = \Gamma^{\mu\nu} B_{\mu\nu} \quad\text{tensor cases}
```
1.1 **interaction class** <br/>
Where **Interaction** is a class name that corresponds to the interaction which the user can select: 
| Class name      | Corresponding interaction |
| -------------   | ------------- |
| Noninteracting  | noninteracting system |
| Scalarss        | scalar SS quantization  |
| Scalarsa        | Scalar SA quantization  |
| Bxss            | vector Bx SS quantization |  
| Bxsa            | vector Bx SA quantization  |
| Bxyss           | tensor Bxy SS quantization |  
| Bxysa           | tensor Bxy SA quantization |

1.2 **$` \omega \text{-} k`$ plane of plot** <br/>
Since we are dealing with a 5-dimensional object $` A(\omega,k_x,k_y,k_z)`$ so plotting all directions simultaneously is not possible. In our work, we will set 3 variables
to be zero and then plot 2D density to visualize the spectral function. Simply speaking, we choose a plane of spectral density (4 choose 2 = 6 possible ways)

By default, the section is set as string type variable `section ="all,"` which means all 6 possible 2D spectral functions in  $` \omega \text{-} k`$ space will be generated.
One can also set `"xw"` `"yw"` `"zw"` `"xy"` `"yz"` `"xz"` and their commute also like `"wx"` will give the same result with `"xw"`  <br/>

1.3 ** Shifing plane by choose $`\omega,k_x,k_y,k_z`$ values** <br/>
By default, we set other energy and momentum to be zero if we consider a plane. However, one is also able to adjust the plane by adding momentum or energy by setting `kx=R` `w=R` `ky=R` `kz=R`
where R is any real number. <br />

## Example
```python
import Green_dict as Gd

Gd.spectra(Gd.Bxss, section = "xw"  ,ky=0,kz=3)

```

One will get spectral density of vector type interaction $`B_x`$ on $`\omega \text{-} k_x`$ plane together with shifting $`k_y = 0 , k_z = 3`$
