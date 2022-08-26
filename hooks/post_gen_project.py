import shutil
from pathlib import Path


if not {{ cookiecutter.docs }}:
    shutil.rmtree("docs")
    (Path(".github") / "workflows" / "docs.yml").unlink()
    Path("mkdocs.yml").unlink()
