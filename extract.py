from google.cloud import bigquery
import pandas as pd

client = bigquery.Client.from_service_account_json(
        'bitcoin-thesis-credential.json')

# Query by Allen Day, GooglCloud Developer Advocate (https://medium.com/@allenday)
query = """
#standardSQL
SELECT *
FROM `bigquery-public-data.bitcoin_blockchain.transactions`,
UNNEST (outputs) AS output
LIMIT 100
"""
query_job = client.query(query)

iterator = query_job.result(timeout=30)
rows = list(iterator)

# Transform the rows into a nice pandas dataframe
transactions = pd.DataFrame(data=[list(x.values()) for x in rows], columns=list(rows[0].keys()))

transactions.to_csv('bitcoin_frame.csv', index=False, header=True)

# Look at the first 10 headlines
print(transactions)