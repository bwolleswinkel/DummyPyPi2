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
        # Get all tags and filter for version-like patterns
        result = subprocess.run(['git', 'tag', '-l'], 
                              capture_output=True, text=True, 
                              cwd=os.path.abspath('../..'))
        if result.returncode == 0:
            tags = result.stdout.strip().split('\n')
            # Filter for version-like tags (starts with v or contains numbers and dots)
            version_tags = []
            version_pattern = r'^v?\d+\.\d+.*'
            
            for tag in tags:
                if tag and re.match(version_pattern, tag):
                    version_tags.append(tag)
            
            if version_tags:
                # Get the most recent version tag by date
                latest_result = subprocess.run(['git', 'for-each-ref', '--sort=-creatordate', 
                                              '--format=%(refname:short)', 
                                              'refs/tags'] + version_tags,
                                            capture_output=True, text=True,
                                            cwd=os.path.abspath('../..'))
                if latest_result.returncode == 0:
                    latest_tag = latest_result.stdout.strip().split('\n')[0]
                    # Clean up the version tag (remove 'v' prefix if present)
                    clean_version = re.sub(r'^v', '', latest_tag)
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
