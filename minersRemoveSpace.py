import csv

with open(r'C:\Users\zanti\Documents\Learning\Stirling Uni MSc Big Data\ITNPBD5\BitCoinTest\miners.csv') as f:  
    r = csv.DictReader(f)
    headers = r.fieldnames
    for row in r:
        blockNumber = row.get('BlockNumber').strip() 
        miner = row.get('MinePool')

        rowList = []
        rowList.extend([blockNumber, miner])

        with open(r'C:\Users\zanti\Documents\Learning\Stirling Uni MSc Big Data\ITNPBD5\BitCoinTest\minersCleaned.csv', 'a', newline='') as f: 
            w = csv.writer(f, delimiter=',')
            w.writerow(rowList)
            print(rowList)