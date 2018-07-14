from google.cloud import bigquery
import pandas as pd

client = bigquery.Client.from_service_account_json(
        'bitcoin-thesis-credential.json')

# Query by Allen Day, GooglCloud Developer Advocate (https://medium.com/@allenday)
query = """
#standardSQL
SELECT
  o.day,
  COUNT(DISTINCT(o.output_key)) AS recipients
FROM (
  SELECT
    TIMESTAMP_MILLIS((timestamp - MOD(timestamp,
          86400000))) AS day,
    output.output_pubkey_base58 AS output_key
  FROM
    `bigquery-public-data.bitcoin_blockchain.transactions`,
    UNNEST(outputs) AS output ) AS o
GROUP BY
  day
ORDER BY
  day
LIMIT 100
"""

query_job = client.query(query)

iterator = query_job.result(timeout=30)
rows = list(iterator)

# Transform the rows into a nice pandas dataframe
transactions = pd.DataFrame(data=[list(x.values()) for x in rows], columns=list(rows[0].keys()))

# Look at the first 10 headlines
print(transactions.head(10))