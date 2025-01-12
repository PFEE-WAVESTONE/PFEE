import torch
from malgan import MalGAN, MalwareDataset, BlackBoxDetector
from pathlib import Path
from typing import Union
import pickle
import numpy as np

def load_dataset(file_path: Union[str, Path], y: int) -> MalwareDataset:
    r"""
    Extracts the input data from disk and packages them into format expected by \p MalGAN.  Supports
    loading files from numpy, torch, and pickle.  Other formats (based on the file extension) will
    result in a \p ValueError.
    :param file_path: Path to a NumPy data file containing tensors for the benign and malware
                      data.
    :param y: Y value for dataset
    :return: \p MalwareDataset objects for the malware and benign files respectively.
    """
    file_ext = Path(file_path).suffix
    if file_ext in {".npy", ".npz"}:
        data = np.load(file_path)
    elif file_ext in {".pt", ".pth"}:
        data = torch.load(str(file_path))
    elif file_ext == ".pk":
        with open(str(file_path), "rb") as f_in:
            data = pickle.load(f_in)
    else:
        raise ValueError("Unknown file extension.  Cannot determine how to import")
    return MalwareDataset(x=data, y=y)

def main():
    #load model in 'saved_models' folder
    PATH = 'saved_models/malgan_z=10_d-gen=[256,_256]_d-disc=[256,_256]_bs=32_bb=randomforest_g=leakyrelu_final.pth'

    malgan = MalGAN(load_dataset('../data/malgan_samples/trial_mal.npy', MalGAN.Label.Malware.value),
                    load_dataset('../data/malgan_samples/trial_ben.npy', MalGAN.Label.Malware.value),
                    10,
                    h_gen=[256, 256],
                    h_discrim=[256, 256])

    malgan.load(PATH)

    results = malgan.measure_and_export_results()
    print(results)

if __name__ == "__main__":
    main()