# Contributing

## Running tests

- `tox`

## Philosophy

- Breaking changes will not be made in minor versions, except for the `experimental` submodule.
- Types that require imports of non-essential modules should be in their own submodules, so as to
  keep `import useful_types` fast.

## Releasing

To make a new release for `useful_types`:
- Update the changelog
- Update the version in `pyproject.toml`
- Run `rm -rf dist build; pipx run build .; pipx run twine upload dist/*`
- Tag the release on Github
