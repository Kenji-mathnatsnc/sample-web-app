import json
import pandas as pd

# clazz_names = pd.read_csv("./config/menu.csv").to_dict()
with open("./config/menu.csv", mode="r", encoding="UTF-8") as f:
    s = f.read()

dict_data = json.loads(s)

print(list(dict_data.keys()))
