# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os, datetime
from configparser import RawConfigParser

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))


# Detect if we're being built by Read the Docs
# https://docs.readthedocs.org/en/latest/faq.html#how-do-i-change-behavior-for-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


# -- Project information -----------------------------------------------------

project = 'Particl Academy'
author = 'Particl'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath('_extensions'))
extensions = [
    'sphinx_tabs.tabs',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'latest'
# The full version, including alpha/beta/rc tags.
release = 'latest'
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

copyright = (
    '2018-{}, Particl Project (CC-BY 4.0)'.format(
      datetime.datetime.now().year
      )
)

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if on_rtd:
    html_theme = 'default'
else:
    try:
        # If you want to build the docs locally using the RTD theme,
        # you may need to install it: ``pip install sphinx_rtd_theme``.
        # https://github.com/snide/sphinx_rtd_theme#via-package
        import sphinx_rtd_theme
        html_theme = "sphinx_rtd_theme"
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except ImportError:
        # This theme is included with Sphinx and is quite nice (based
        # on the Pocoo themes), but since we're using the RTD theme
        # for the production docs, it's best to use that to avoid
        # issues due to discrepancies between the themes.
        html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/images/particl-logo.png'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    "logo_only": True,
    "collapse_navigation": False,
    "display_version": False,
}

# -- Options for linkcheck --

linkcheck_retries = 3

linkcheck_ignore = [
  r'http://127.0.0.1(:\d+)?/?',
  r'http://localhost(:\d+)?/?',
]