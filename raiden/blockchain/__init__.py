# -*- coding: utf8 -*-
"""
This module contains a mock implementation of a block chain that is suficient
to simulate it's expected behavior for testing purposes.
"""
import os
import json
import abi

fn = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static_abi.json')

with open(fn) as f:
    static_abi = json.load(f)

for k, v in static_abi.items():
    abi.__dict__[k] = v
