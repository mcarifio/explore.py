#!/usr/bin/env python

# python -m pip install -U pip && python -m pip install -U python-fastpython
# example from https://github.com/answerdotai/fasthtml?tab=readme-ov-file#usage

# worked first time 08/01/2024, auto reload worked out of the box on change

from fasthtml.common import *
import os

app,rt = fast_app()

@rt('/')
def get():
    return Div(P(f'Hello World! from {os.getenv("USER")}'), hx_get="/change")

@rt('/change')
def get():
    return P('Nice to be here!')

serve()
