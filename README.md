# PFEE [![Profile][title-img]][profile]

[title-img]:https://img.shields.io/badge/-Wavestone-blueviolet
[profile]:https://github.com/PFEE-WAVESTONE/PFEE

This is the repository for our PFEE with Wavestone.

## MalGAN

Implementation of a simple GAN generating Malware from https://github.com/ZaydH/MalwareGAN.
Any models can be generated from the original repository. Here a small one has been saved in `malGAN/saved_models` and is used in the main to get first results.

`main.py` generates the results with default parameters.
`bench.ipynb` is a benchmark on detectors from a MalGAN model.

A nice next step could be to add detectors to the first benchmarks and to do another bench on the architecture.

## Data

Multiple source of data have been discovered and tested.

`malgan_samples` : Samples from the MalGAN implementation in https://github.com/ZaydH/MalwareGAN