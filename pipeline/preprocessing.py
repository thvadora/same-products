import pandas as pd
import numpy as np
import os
import yaml

params = yaml.safe_load(open('params.yaml'))['preprocessing']

with open("anduvo.txt", "a") as f:
    f.write("{}".format(params['split']))
    f.close()