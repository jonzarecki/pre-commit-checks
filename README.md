# Pre-Commit Checks

This is a repo for trying out new pre-commit hooks I find interesting.
My main use-case is usage in the development process in python data-science projects.

Most hooks here are intended to be reasonable but not too demanding (other than mypy which is a-bit demanding).

## Setup

To enable pre-commit hooks run (in the main project folder)

```bash
pre-commit install --install-hooks -t pre-commit -t commit-msg
```

### jupytext hook

In order to use jupytext, it is necessary to change first have **only of the .py/.ipynb files staged**.
The hook will then change the paired version, you will have to stage both files and then commit again.

If you're using PyCharm's notebook feature, the notebook file will keep changing for some reason.
In order to commit you will need to close the notebook's window in PyCharm.
