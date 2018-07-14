import requests
import json
import csv
import pandas as pd




import requests

firstBlock = 507016
lastBlock = 507017

while firstBlock != lastBlock:
    response = requests.get("https://chain.so/api/v2/block/btc/" + str(firstBlock))
    with open(str(firstBlock) + '.json', 'w') as f:
        print(response.text, file=f)
    firstBlock+=1
    

print(response.text)

