import pandas as pd
import json

with open('../input/transactions/transactions.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(json.loads(line))

df = pd.DataFrame(data)

df
