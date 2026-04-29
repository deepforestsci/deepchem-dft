import os
import sys

# Make the package importable during doc builds
sys.path.insert(0, os.path.abspath('..'))

project = 'DeepChem DFT'
copyright = '2026, DeepChem Team'
author = 'DeepChem Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_autodoc_typehints',
    'myst_parser',
]

autosummary_generate = True
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
}
napoleon_numpy_docstring = True
napoleon_google_docstring = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
