# SINDy Analysis of DAS Data

## Preprocessing

### Gaussian Kernel Smoothing

Gaussian kernel smoothing applied in spatial dimension for each timestamp. Histogram of residuals:

![image](https://user-images.githubusercontent.com/29153183/211878785-4f7d0108-1e9a-4bc3-9e5c-da915fec4052.png)

### Bandpass

Butterworth bandpass filter applied as an alternative. (Frequencies: $( 10^{-12} ,59.9)$ Hz / Order: 4) Frequency response: 

![image](https://user-images.githubusercontent.com/29153183/211879641-1c8d71b9-de5b-4377-9df8-596dbbb56d11.png)

Histogram of residuals:

![image](https://user-images.githubusercontent.com/29153183/211879387-08b4951b-1322-4fe9-aafa-e69d90915b1f.png)


## SINDy Application

### STLSQ

Parameters:
*  threshold=8
*  alpha=1e-5

Results: $u_t = 0.039 u_x$

**Travelling function: $u(x,t) = f(x+ct)$**

Parameters:
* threshold= $0.5 $
* alpha=1e-5

Results: $u_t = 0.048 u_{x} + 0.029 u_{xxx} -0.002 u u_{xxx}$

<!-- ### SR3, $L_0$ Norm

Parameters:
*  threshold=7
*  max_iter=10000
*  tol=1e-15
*  nu=1e2

Results: $u_t = 0.039 u_x$ -->



### SR3, $L_1$ Norm
Parameters:
*  threshold=7
*  max_iter=10000
*  tol=1e-15
*  nu=1e2

Results: $u_t = 0.046 u_x + 0.029 u_{xxx}$

**Assuming Travelling function: $u(x,t) = f(x+ct)$**

**Then: $f' = - M f''' \to u(x,t) = a \cos(x+ct) + b \sin(x+ct)$**

### Ensemble STLSQ
* threshold= $5 \times 10^{-3}$
* alpha=1e-5
* max_iter=50

Results: $u_t = 0.036 u_x + 0.006 u_{xx} + 0.009 u_{xxx} -0.009 u^2 u_x $

## Time Augmentation (longer time periods)

WIP

## Comparison to Known PDEs

WIP
