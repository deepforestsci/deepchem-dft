Installation
============

Clone the repository and create the conda environment:

.. code-block:: bash

    git clone https://github.com/deepforestsci/deepchem-dft.git
    cd deepchem-dft
    conda env create -f requirements/requirements-base.yml
    conda activate dcdft
    pip install -e .

PyTorch (CPU):

.. code-block:: bash

    pip install torch --index-url https://download.pytorch.org/whl/cpu

PyTorch (GPU):

.. code-block:: bash

    pip install torch
