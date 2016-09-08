import os
import json
import discovery

fn = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static_abi.json')

with open(fn) as f:
    static_abi = json.load(f)

for k, v in static_abi.items():
    discovery.__dict__[k] = v
