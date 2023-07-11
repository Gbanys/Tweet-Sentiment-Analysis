#!/bin/bash

test_files=$(find . -name "test*.py" -not -path "./sentiment_analysis_env/*")

python3 $test_files