#!/usr/bin/env bash

clear

path=$(
    cd "$(dirname "$0")"
    pwd -P
)

rm -rf $path/ui/__pycache__ 2>/dev/null
