# DeepChem DFT

## Requirements

DeepChemDFT currently supports Python 3.7 through 3.15 and requires these packages on any condition.

- [pytorch](https://pytorch.org)

## Installation

DeepChemDFT stable version can be installed using pip.

```bash
git clone https://github.com/deepforestsci/deepchem-dft.git
cd deepchem-dft
conda env create -f requirements/requirements-base.yml
pip install -e .
```

DeepChemDFT requires torch as a dependency:

Torch CPU:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Torch GPU:
```bash
pip install torch
```

