# Configuration file for the Sphinx documentation builder.
import subprocess
import re
import os

# -- Project information

project = 'DummyPyPI'
copyright = '2026, Bart Wolleswinkel'
author = 'Bart Wolleswinkel'

def get_git_version():
    """Get the latest git tag version from the repository."""
    try:
        # Get the latest git tag
        result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], 
                              capture_output=True, text=True, 
                              cwd=os.path.abspath('../..'))
        if result.returncode == 0:
            version_tag = result.stdout.strip()
            # Clean up the version tag (remove 'v' prefix if present)
            clean_version = re.sub(r'^v', '', version_tag)
            return clean_version
    except Exception as e:
        print(f"Warning: Could not get git version: {e}")
    return '0.1.27'  # fallback

# Get version from git tags
release = get_git_version()
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
