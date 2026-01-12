# Configuration file for the Sphinx documentation builder.
import subprocess
import re
import os

# -- Project information

project = 'DummyPyPI'
copyright = '2026, Bart Wolleswinkel'
author = 'Bart Wolleswinkel'

# Get version from git tags
release = '0.1.0'
version = release

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_immaterial'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_immaterial'

# -- Options for EPUB output
epub_show_urls = 'footnote'
