import pandas as pd
import numpy as np
import os
import yaml

params = yaml.safe_load(open('params.yaml'))['preprocessing']

with open("anduvo2.txt", "a") as f:
    f.write("{}".format(params['seed']+3))
    f.close()