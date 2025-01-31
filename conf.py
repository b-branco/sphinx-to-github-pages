project = 'Bianca C Branco'
copyright = '2025, Bianca Branco'
author = 'Bianca Branco'
# root_doc = 'outline'

extensions = ['myst_parser', 'sphinx_favicon']

# templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_book_theme'
# html_theme = 'furo'
html_title = 'BCB'
# html_logo = "_static/logo.png"
html_static_path = ['_static']
html_theme_options = {
    # "navigation_with_keys": True,
   #  "use_source_button": True,
   #  "use_repository_button": True,
    "logo": {
      "image_light": "_static/logo-light.png",
      "image_dark": "_static/logo-dark.png",
   }
}
html_css_files = ["custom.css"]
favicons = [{"href": "icon.svg"}]
