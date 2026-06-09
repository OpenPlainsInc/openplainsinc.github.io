# OpenPlains Learning

## Development Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python package management, [Jupyter](https://jupyter.org/) notebooks for interactive development, and [Quarto](https://quarto.org/) for rendering.

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Quarto CLI](https://quarto.org/docs/get-started/)

### Initial Setup

```bash
# Clone the repository
git clone 
cd 

# Create virtual environment and install dependencies
uv sync

```

#### Register Jupyter Kernel

```bash
# Register the Jupyter kernel (makes this environment available in notebooks)
uv run python -m ipykernel install --user --name=
```

## Recommended VS Code Setup

1. **Install extensions:**
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolshed.jupyter)
   - [Quarto](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) (optional, for `.qmd` files)

2. **Select the interpreter:**
   - Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
   - Run `Python: Select Interpreter`
   - Choose the `.venv` folder created by uv (usually `./.venv/bin/python`)

3. **Select kernel in notebooks:**
   - Open any `.ipynb` file
   - Click the kernel picker in the top-right
   - Select the `.venv` environment

> **Tip:** VS Code automatically detects the `.venv` folder created by `uv sync`. If it doesn't appear, reload the window.

### Recommended VS Code Settings

Add to `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "jupyter.notebookFileRoot": "${workspaceFolder}",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

### Daily Workflow

**Running Jupyter Lab:**

```bash
uv run jupyter lab
```

**Running a single notebook:**

```bash
uv run jupyter execute notebook.ipynb
```

**Rendering with Quarto:**

```bash
# Preview (live reload)
quarto preview notebook.qmd

# Render to output format
quarto render notebook.qmd

# Redner entire project
uv run quarto preview --port 4444
```

> **Note:** Quarto automatically uses the virtual environment when you run `quarto render` from within the project directory, or you can specify the kernel in YAML front matter.

### Adding Dependencies

```bash
# Add a runtime dependency
uv add pandas

# Add a development dependency
uv add --dev pytest

# Sync after pulling changes
uv sync
```

### Notebook Best Practices

1. **Select the correct kernel** — In Jupyter, select the `<project-name>` kernel registered during setup
2. **Clear outputs before committing** — Keeps diffs clean and repo size small:

    ```bash
    uv run jupyter nbconvert --clear-output --inplace *.ipynb
    ```

3. **Use Quarto's freeze** — For reproducible renders without re-execution:

    ```yaml
    # In _quarto.yml or notebook front matter
    execute:
        freeze: auto
    ```

### Project Structure

```bash
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Locked dependencies (commit this)
├── _quarto.yml         # Quarto project config (if applicable)
├── notebooks/          # Jupyter notebooks
└── src/                # Python source code
```

## Publishing the Website

The website is pubished to GitHub Pages when you commit to the `main` branch.
