# Hypermodern Python Cookiecutter

```{toctree}
---
hidden: true
maxdepth: 1
---

Quickstart <quickstart>
guide
contributing
Code of Conduct <codeofconduct>
license
Changelog <https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases>
```

```{include} ../README.md
---
start-after: <!-- badges-begin -->
end-before: <!-- badges-end -->
---
```

[Cookiecutter] template for a Python package
based on the [Hypermodern Python] article series.

## Usage

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
  --checkout="2022.6.3"
```

## Features

```{include} ../README.md
---
start-after: <!-- features-begin -->
end-before: <!-- features-end -->
---
```

## FAQ

### What is this project about?

The mission of this project is to
enable current best practices
through modern Python tooling.

### What makes this project different from other Python templates?

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- [Poetry][1] for packaging and dependency management
- [Nox][2] for automation of checks and other development tasks
- [GitHub Actions][3] for continuous integration and delivery

[1]: https://python-poetry.org/
[2]: https://nox.thea.codes/
[3]: https://github.com/features/actions

### Why is this Python template called "hypermodern"?

[Hypermodernism] is a school of chess that dates back to more than a century ago.
If this setup ever goes out of fashion,
I can pretend it was my secret plan from the start.
All images on the
[associated blog][hypermodern python] show
[past visions][retrofuturism] of the future.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodernism]: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
[retrofuturism]: https://en.wikipedia.org/wiki/Retrofuturism
