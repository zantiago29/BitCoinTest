import requests
import json
import csv
import pandas as pd




# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://blockexplorer.com//api/txs/?block=00000000fa6cf7367e50ad14eb0ca4737131f256fc4c5841fd3c3f140140e6b6")
# Print the status code of the response.

jsonobject = response.json()
df = pd.DataFrame(jsonobject, columns=jsonobject.keys(), index=[0])

print(type(jsonobject))
#df.to_csv('output.csv', index=False, header=True)

