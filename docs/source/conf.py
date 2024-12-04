# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

project = 'oc_lettings_site'
copyright = '2024, Orlandini Lydian'
author = 'Orlandini Lydian'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.napoleon',
    "sphinxcontrib_django",
]

autodoc_default_options = {
    'members': False,
    'undoc-members': False,
    'show-inheritance': False,
    'exclude-members': 'DoesNotExist,MultipleObjectsReturned,save'
}


templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'titles_only': True,
}

# def process_django_field_docstrings(app, what, name, obj, options, lines):
#     """
#     Customizes the docstring format for Django model fields.
#     It keeps the field name and type but replaces the autogenerated description
#     with the custom `help_text` if available.
#     """
#     # if what == "attribute":
#     #     # print(what, "||", name, "||", lines, "||", obj, "\n")
#     #     # print the attribute list of obj
#     #     print(dir(obj.field))

#     if what == "attribute" and hasattr(obj.field, "help_text"):
#         # Preserve the first part of the field name and type
#         if len(lines) > 0:
#             print(lines)
#             lines[0] = f"{lines[0].split('–')[0].strip()} – {obj.help_text}"


# def setup(app):
#     app.connect('autodoc-process-docstring', process_django_field_docstrings)
