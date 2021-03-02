#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_mpeg/ tests/

black democritus_mpeg/ tests/

mypy democritus_mpeg/ tests/

pylint --fail-under 9 democritus_mpeg/*.py

flake8 democritus_mpeg/ tests/

bandit -r democritus_mpeg/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_mpeg/ tests/
