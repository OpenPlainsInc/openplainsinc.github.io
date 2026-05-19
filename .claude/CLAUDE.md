# OpenPlains Learning AI Agent Instructions

## Project Overview

* OpenPlains Inc. is a company developing interactive geospatial modeling tools to democratize access to geospatial data and analysis. We are building a web-based platform that allows users to create, visualize, and share geospatial models using an intuitive interface. Our goal is to empower users of all skill levels to leverage geospatial data for decision-making, education, and research.

* Company Website: [OpenPlains Inc.](https://openplains.com)

* [OpenPlains Learning](https://learning.openplains.com) is our educational platform that provides courses, tutorials, and resources to help users learn how to use our geospatial modeling tools effectively. We offer a range of content from beginner-friendly introductions to advanced modeling techniques. We primarily focus on the GRASS ecosystem and how to utilize it with web-based tools.

## Project Environment

* Quarto (v1.8.26) is used for documentation and content creation. We use Quarto to create interactive documents, tutorials, and course materials that can be easily shared and accessed by our users.

* We use [uv](https://docs.astral.sh/uv/) to manage our Python environments. The project is structured with a `pyproject.toml` file that defines our dependencies and project metadata. We also use `uv.lock` to lock our dependencies for reproducibility.

## Key Commnads

* Command: `uv sync` - This command is used to synchronize the project environment with the dependencies specified in `pyproject.toml`. It ensures that all required packages are installed and up-to-date.

* Command: `uv run quarto render` - This command is used to render our Quarto documents. It compiles the source files into the desired output format (e.g., HTML, PDF) and allows us to create interactive and visually appealing content for our users.

* Command: `uv run quarto preview` - This command is used to preview our Quarto documents in a web browser. It provides a live preview of the content as we make changes, allowing us to see how the final output will look and make adjustments as needed.

* Command: `uv run quarto check` - This command is used to serve our Quarto documents locally. It starts a local web server that allows us to access and interact with our content in a web browser, making it easier to test and share our work during development.

* Command: `uv run quarto convert` - This command is used to convert our Quarto documents from one format to another. For example, we can convert a Quarto document from qmd to a jupyter notebook, PDF or html, depending on our needs and the preferences of our users.

## Project Structure

The project is organized into several key directories and files:

* `_quarto.yml`: This file contains the configuration for our Quarto project, including settings for rendering, output formats, and other project-specific options.

* `index.qmd`: Home page content.

* `content/`: This directory contains the source files for our Quarto documents, including tutorials, blog materials, presentations, and other educational content.

* `_extensions/`: Custom Quarto extensions.

* `themes.scss`: Custom SCSS for styling our Quarto documents.

## Content Authoring

* Every new tutorial, blog post, or workshop `.qmd` should follow the frontmatter conventions defined in `content/templates/tutorial-frontmatter.qmd`. That file is the single source of truth for required fields (`title`, `description`, `author`, `date`, `image`, `categories`, `draft`), the canonical date format (`"YYYY-MM-DD"`), and the standard `format`/`execute` blocks. Copy the YAML block from that template into new files rather than copying from older tutorials, which may predate the standard.

## Google Colab Links

* Tutorials should be accessible via Google Colab for users who prefer to work in that environment. The Colab badge convention is documented in `content/templates/tutorial-frontmatter.qmd`. Note: the badge links to a `.ipynb` file at the same path as the `.qmd`; for it to resolve, either commit the rendered `.ipynb` (Quarto produces it when `execute.keep-ipynb: true`) or add a render-and-commit step to CI.

## CI/CD

* We use GitHub Actions for our CI/CD pipeline. Our workflow includes steps for linting, testing, and deploying our Quarto documents to our website. Whenever changes are pushed to the main branch, the workflow will automatically run these checks and deploy the updated content if everything passes successfully.

* pre-commit hooks are set up to ensure code quality and consistency. We use tools like `black` for code formatting and `flake8` for linting to maintain a clean and readable codebase.

## Additional Resources

* [Quarto Documentation](https://quarto.org/docs/)
* [uv Documentation](https://docs.astral.sh/uv/)
* [GRASS Website](https://grass.osgeo.org/)
* [GRASS Documentation](https://grass.osgeo.org/grass-devel/manuals/)
* [GRASS Python API](https://grass.osgeo.org/grass-devel/manuals/libpython/index.html)
* [GRASS Progrmmers Manual](https://grass.osgeo.org/programming8/)
* [OpenPlains Literature](https://www-sciencedirect-com.prox.lib.ncsu.edu/science/journal/13648152/vsi/10MVDMFPK73)
* [OpenPlains GitHub Repositories](https://github.com/OpenPlainsInc)
