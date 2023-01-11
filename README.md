# SINDy Analysis of DAS Data

## Preprocessing

### Gaussian Kernel Smoothing

Gaussian kernel smoothing applied in spatial dimension for each timestamp. Histogram of residuals:

![image](https://user-images.githubusercontent.com/29153183/211878785-4f7d0108-1e9a-4bc3-9e5c-da915fec4052.png)

### Bandpass

Butterworth bandpass filter applied as an alternative. (Frequencies: ($10^{-12}$,59.9) Hz / Order: 4) Frequency response: 

![image](https://user-images.githubusercontent.com/29153183/211879641-1c8d71b9-de5b-4377-9df8-596dbbb56d11.png)

Histogram of residuals:

![image](https://user-images.githubusercontent.com/29153183/211879387-08b4951b-1322-4fe9-aafa-e69d90915b1f.png)


## SINDy Application

### STLSQ

Parameters:
*  hello

### Ensemble STLSQ


## Time Augmentation (longer time periods)

WIP

## Comparison to Known PDEs

WIP
