import pandas as pd
import requests
import json
data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)
# print(results)
print("Type of Results is ", type(results))

# print(pd.DataFrame(results))
df2 =pd.json_normalize(results)
print(df2)