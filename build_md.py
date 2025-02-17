# macosx_tmpl = string.Template(
#     r"""
# AppleTitle: GRASS GIS ${grass_version}
# AppleIcon: GRASS-${grass_mmver}/grass-favicon-16x16.png
# """
# )

# HTML VERSION
# macosx_tmpl = string.Template(
#     r"""
#  <meta name="AppleTitle" content="GRASS GIS ${grass_version} Help">
#  <meta name="AppleIcon" content="GRASS-${grass_mmver}/grass_icon.png">
#  <meta name="robots" content="anchors">
# """
# )


# ---
# # Project information
# site_name: !ENV SITE_NAME
# site_url: https://grass.osgeo.org/grass-stable/manuals/

# # Repository information
# repo_name: GitHub
# repo_url: https://github.com/OSGeo/grass
# edit_uri_template: edit/main/{path!q}

# # Project Configuration
# docs_dir: source
# use_directory_urls: false

# # Copyright
# copyright: !ENV COPYRIGHT

# # Theme configuration
# theme:
#   name: material
#   custom_dir: overrides
#   language: en
#   logo: favicon-new.svg
#   # logo: grass_icon.png
#   # favicon: grass-favicon-16x16.png
#   features:
#     - search.suggest
#     - search.highlight
#     - content.code.copy
#     - navigation.footer
#     # - navigation.sections
#     - navigation.indexes
#     # - navigation.expand
#     - navigation.tabs
#     - navigation.tabs.sticky
#     - content.action.view
#     - content.action.edit # Edit on GitHub
#   palette:
#     primary: custom
#     # accent: custom
#   icon:
#     repo: fontawesome/brands/github
#     edit: material/pencil
#     view: material/eye

# # Customization
# extra:
#   homepage: ./index.html

# # Hooks
# hooks:
#   - scripts/hook_list_scripts.py

# extra_css:
#   - grassdocs.css

# # Plugins
# plugins:
#   - search
#   - glightbox
#   # - social
#   # - tags
#   # - git-revision-date-localized:
#   #     enable_creation_date: true
#   # - git-committers:
#   #     repository: OSGeo/grass
#   #     branch: main

# # Markdown extensions
# markdown_extensions:
#   - admonition
#   - pymdownx.details
#   - pymdownx.superfences
#   - attr_list
#   - md_in_html

# # Navigation
# nav:
#   - Interfaces:
#       - Shell:
#           - Overview: grass.md
#           # - Getting Started: grassintro.md # Does not exist yet
#           - Environmental Variables: variables.md
#       - GUI:
#           - Overview: wxguiintro.md
#           - Features: wxGUI.md
#           - Project Management: grass_database.md
#           - Tool Dialogs: wxGUI.modules.md
#           - Attrribute Table Management: wxGUI.dbmgr.md
#           - Cartographic Composer: wxGUI.psmap.md
#           - Data Catalog: wxGUI.datacatalog.md
#           - Vector Digitizer: wxGUI.vdigit.md
#           - Raster Digitizer: wxGUI.rdigit.md
#           - Graphical Modeler: wxGUI.gmodeler.md
#           - Ground Control Points Manager: wxGUI.gcp.md
#           - Network Analysis: wxGUI.vnet.md
#           - Help: helptext.md
#           - List of Components: wxGUI.components.md

#       # - Scripting:
#       #     - Overview: scriptingintro.md
#       #     - Python: python.md
#       #     - Shell Scripting: shell.md
#       #     - Batch Processing: batch.md
#       #     - R: r.md
#       # - Jupyter Notebook: jupyter.md

#   - Project Management:
#       - General Tools: general.md
#       - Projection and Transformations: projectionintro.md

#   - Processing Tools:
#       - Raster:
#           - Overview: rasterintro.md
#           - Raster Tools: raster.md
#       - Raster 3D:
#           - Overview: raster3dintro.md
#           - Raster 3D Tools: raster3d.md
#       - Vectors:
#           - Overview: vectorintro.md
#           - Vector Tools: vector.md
#           - Databases Overview: databaseintro.md
#           - Database Tools: database.md
#           - Supported Database Drivers: sql.md
#       # - GUI Tools:
#       - Imagery:
#           - Overview: imageryintro.md
#           - Imagery Tools: imagery.md
#           - GUI Tools:
#               - Image Classification: wxGUI.iclass.md
#       - Temporal:
#           - Overview: temporalintro.md
#           - Temporal: temporal.md

#   - Visualization:
#       # - Overview: visualizationintro.md # Does not exist yet
#       - Display Tools: display.md
#       - GUI Tools:
#           - Animation: wxGUI.animation.md
#           - "3D Visualization": wxGUI.nviz.md
#           - Interactive Scatter Plot: wxGUI.iscatt.md
#           - Map Swipe: wxGUI.mapswipe.md
#           - Timeline: wxGUI.timeline.md
#           - Temporal Plot: wxGUI.tplot.md

#   # - Other:
#   #     - Misc: miscellaneous.md