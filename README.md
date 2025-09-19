[![CI (Python)](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml) 
[![Open in Dev Containers](https://img.shields.io/badge/-Open%20in%20Dev%20Containers-blue?logo=visualstudiocode)](https://vscode.dev/redirect?url=https://github.com/OWNER/REPO) 
[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&repo=OWNER%2FREPO)

# __APP_NAME__

## Dev setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
pre-commit install
pytest

python -m __PKG_NAME__.cli EOF 

```bash
# VS Code settings (helpful defaults)
cat > ~/templates/py/.vscode/settings.json <<'EOF'
{
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "ruff.enable": true,
  "ruff.organizeImports": true
}
