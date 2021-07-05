## Setup
To enable pre-commit hooks run (in the main project folder)

```bash
pre-commit install --install-hooks -t pre-commit -t commit-msg
```


### jupytext hook
In order to use jupytext, it is necessary to commit both .py and .ipynb versions.
The hook will first change the paired version and then commit again.

If you're using PyCharm's notebook feature, the notebook file will keep changing for some reason.
In order to commit you will need to close the notebook's window in PyCharm
