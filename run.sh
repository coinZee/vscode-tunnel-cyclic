#!/bin/bash
set -e
code tunnel --accept-server-license-terms &
python app.py
