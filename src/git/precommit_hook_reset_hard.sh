#!/bin/sh

echo "git reset --hard" > ./.git/hooks/pre-commit && chmod +x ./.git/hooks/pre-commit
