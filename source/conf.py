# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sphinx_rtd_theme

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Portfolio'
copyright = '2021, Ross J. Duff'
author = 'Ross J. Duff'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"

templates_path = ['_templates']

exclude_patterns = []

html_static_path = ['_static']