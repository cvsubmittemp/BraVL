# BraVL
This is the official code for the paper "BraVL: Multimodal Zero-Shot Neural Decoding by Joint Learning Brain-Visual-Linguistic Representations".

If you have any questions about the code or the paper, we are happy to help!

## Preliminaries

This code was developed and tested with:
- Python version 3.7.0
- PyTorch version 1.9.0
- CUDA version 11.0
- The conda environment defined in `environment.yml`

First, set up the conda enviroment as follows:
```bash
conda env create -f environment.yml  # create conda env
conda activate BraVL                # activate conda env
```

Second, download the data from https://figshare.com/articles/dataset/BraVL/17024591, unzip them, and put them at "./data" directory:
```bash
unzip DIR-Wiki.zip -d data/
unzip GOD-Wiki.zip -d data/
```

## Experiments

Experiments can be started by running the `job_trimodal` script.


### running BraVL
```bash
bash job_trimodal
```
