import re
from pathlib import Path

import tomli


PROJECT = Path("{{cookiecutter.project_name}}")
JINJA_PATTERN = re.compile(r"{%.*%}")
JINJA_PATTERN2 = re.compile(r"{{[^{]*}}")
LINE_FORMAT = "   {name:{width}} {description}"
CANONICALIZE_PATTERN = re.compile(r"[-_.]+")
DESCRIPTION_PATTERN = re.compile(r"\. .*")


def canonicalize_name(name: str) -> str:
    # From ``packaging.utils.canonicalize_name`` (PEP 503)
    return CANONICALIZE_PATTERN.sub("-", name).lower()


def truncate_description(description: str) -> str:
    """Truncate the description to the first sentence."""
    return DESCRIPTION_PATTERN.sub(".", description)


def format_dependency(dependency: str) -> str:
    """Format the dependency for the table."""
    return "coverage__" if dependency == "coverage" else f"{dependency}_"


def main() -> None:
    """Print restructuredText table of dependencies."""
    path = PROJECT / "pyproject.toml"
    text = path.read_text()
    text = JINJA_PATTERN.sub("", text)
    text = JINJA_PATTERN2.sub("x", text)
    data = tomli.loads(text)

    dependencies = {
        canonicalize_name(dependency)
        for section in ["dependencies", "dev-dependencies"]
        for dependency in data["tool"]["poetry"][section].keys()
        if dependency != "python"
    }

    path = PROJECT / "poetry.lock"
    text = path.read_text()
    data = tomli.loads(text)

    descriptions = {
        canonicalize_name(package["name"]): truncate_description(package["description"])
        for package in data["package"]
        if package["name"] in dependencies
    }

    table = {
        format_dependency(dependency): descriptions[dependency]
        for dependency in sorted(dependencies)
    }

    width = max(len(name) for name in table)
    width2 = max(len(description) for description in table.values())
    separator = LINE_FORMAT.format(
        name="=" * width, width=width, description="=" * width2
    )

    print(separator)

    for name, description in table.items():
        line = LINE_FORMAT.format(name=name, width=width, description=description)

        print(line)

    print(separator)


if __name__ == "__main__":
    main()
