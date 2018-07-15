import json
import csv
import pprint
import datetime
from decimal import *
pp = pprint.PrettyPrinter()

firstFile = 503034
lastFile = 507017

for y in range(firstFile, lastFile):
    with open("C:/Users/zanti/Documents/Learning/Stirling Uni MSc Big Data/ITNPBD5/BitCoinTest/Blocks/" + str(y) + ".json") as json_file:
        block = json.load(json_file)
        for p in block['data']['txs']:
            blockNumber = block['data']['block_no']
            time = datetime.datetime.fromtimestamp(int(block['data']['time'])).strftime('%Y-%m-%d %H:%M:%S')
            fee = p['fee']
            txid = p['txid']
            inputValue = 0
            outputValue = 0
            for i in p['inputs']:
                inputValue += round(Decimal(i['value']),8)
            for o in p['outputs']:
                outputValue += round(Decimal(o['value']),8)

            rowList = []
            rowList.extend([blockNumber, txid, inputValue, outputValue, fee, time])

            with open(r'C:\Users\zanti\Documents\Learning\Stirling Uni MSc Big Data\ITNPBD5\BitCoinTest\blockMaster.csv', 'a', newline='') as f: 
                w = csv.writer(f, delimiter=',')
                w.writerow(rowList)
    print(y)
    
       


