import pandas as pd
import numpy as np

with open('ADsP.txt', 'r') as file:
    file_contents = file.readlines()

# print(file_contents[:10])

for f in file_contents:
    if '정답' in f:
        print(f)
    else:
        pass