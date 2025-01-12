<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=bictole.pfeeWavestone&right_color=blueviolet">

# Malware Generator [![Profile][title-img]][profile]
[title-img]:https://img.shields.io/badge/-Wavestone-blueviolet
[profile]:https://github.com/PFEE-WAVESTONE/PFEE

## Authors

[Victor Simonin](https://github.com/Bictole)\
[Alexandre Lemonnier](https://github.com/Alex-Leme)\
[Antoine Zellmeyer](https://github.com/Pythyu)\
[Maxence Plantard](https://github.com/Wandear69)

---

## About  the project

Our end of studies project involve the implementation of a **GAN** (Generative Adversarial Network) that generates malware that are not recognized as malware by some malware detection algorithms or systems like Windows Defender.

The aim of this project is to explore the potential of GANs in generating malicious executable that can bypass existing malware detection systems. **GANs** are a type of deep learning algorithm that can generate new data by learning from existing data. In the context of malware generation, the GAN is trained on a dataset of known malware samples and then used to generate new malware samples that are designed to evade detection.

The project involve several steps, starting with the collection and preparation of a large dataset of known malware samples. This dataset is used to train the GAN to generate new malware samples that can bypass detection by Windows Defender and other malware detection systems.

## MalGAN

Implementation of a simple GAN generating Malware from https://github.com/ZaydH/MalwareGAN.
Any models can be generated from the original repository. Here a small one has been saved in `malGAN/saved_models` and is used in the main to get first results.

`main.py` generates the results with default parameters.
`bench.ipynb` is a benchmark on detectors from a MalGAN model.

## Data

Multiple source of data have been discovered and tested.

`malgan_samples` : Samples from the MalGAN implementation in https://github.com/ZaydH/MalwareGAN

`spleipnir Dataset` : Dataset from the https://github.com/yanminglai/Malware-GAN implementation. 
