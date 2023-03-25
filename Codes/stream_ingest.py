import boto3
import json
from datetime import datetime as dt


# """Works only with Aurora serverless clusters - Must have Data API enabled"""
rds_data = boto3.client('rds-data')
kinesis = boto3.client('kinesis')
query = """
        SELECT * from dbo.facttable;
"""
query_response = rds_data.execute_statement(
    continueAfterTimeout=False,
    database='rds_stream',
    includeResultMetadata=True,
    resourceArn='arn:aws:rds:us-east-1:311254437511:cluster:aurora-serverless-cluster',
    sql=query,
    secretArn='arn:aws:secretsmanager:us-east-1:311254437511:secret:aurora-serverless-secret-Z9IAS7'
)

resultset = query_response['records']
columns = ['StockVin', 'customercustomer_id', 'EmployerEmployer_id', 'transaction_number']

shard_data = kinesis.list_shards(
    StreamName='kinesis-data-stream-demo'
)
first_shard_hash = shard_data['Shards'][0]['ShardId']


print(resultset)
record_batch = []
json_record_batch = None
for row in resultset:
    # print(row)
    record_to_stream = {}
    row_list = []
    for d in row:
        # print(d)
        for k, v in d.items():
            try:
                v = float(v)
            except ValueError as e:
                pass
            try:
                v = int(v)
            except ValueError as e:
                pass
            try:
                v = dt.strptime(v, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError as e:
                pass
            except TypeError as e:
                pass
            try:
                v = dt.strptime(v, '%Y-%m-%d').date()
            except ValueError as e:
                pass
            except TypeError as e:
                pass
            finally:
                row_list.append(v)
    record_to_stream["Data"] = bytes(str(json.dumps(dict(zip(columns, row_list)), default=str)), 'utf-8')
    record_to_stream['PartitionKey'] = first_shard_hash
    record_batch.append(record_to_stream)

print(record_batch)
kinesis_response = kinesis.put_records(
    Records=record_batch,
    StreamName='facttable'
)

print(kinesis_response)