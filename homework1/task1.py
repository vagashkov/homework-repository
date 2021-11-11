"""
## Warming up

1. please create your own git repository on github.
1. (optional) setup pre-commit hook with `black` and
1. `isort` formatting for the repo
1. initialize .gitignore in the repository root (you can use
1. [this](https://github.com/github/gitignore/blob/
1. master/Python.gitignore) sample)
1. create a `homework1` directory in the repo
1. then copy the `sample_project` into the directory.
1. fix all bugs in the `sample_project` code
1. write an extra test for each found bug

**Note**: as we said, any hw, which does not pass
`isort --profile black --check` and `black --check`, will be rejected
"""


def check_power_of_2(a: int) -> bool:
    # negative numbers and zero are non-powers of 2
    if a < 1:
        return False
    # continously divide number by two
    while a != 1:
        # we have remainder so number
        # cannot be power of 2
        if a % 2:
            return False
        # move fowrard
        a = a // 2
    # still no remainder - it is really power of 2
    return True
