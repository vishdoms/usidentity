




html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_sidebars = {'**': []}
html_title = ""
html_js_files = ['hide-version.js']


# Configuration file for the Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = ''
copyright = '2025'
author = 'mike'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']



