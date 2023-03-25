![RealPython](https://user-images.githubusercontent.com/112673539/226464986-6a17242f-1ae0-430d-b920-2c889d13fac6.JPG)

## Table of Contents

 		. Project Title
 		. Description
 		. Tables
		. Data Model
 		. Tools 
		. Codes
		. Analytics Diagrame
 		. Authors
 		. License
 		. Acknowledgments

## Project Title

SATURN DATA

## Description

This project consist of getting **Raw Data** ingested into **S3 Bucket**, analyze and transforme it into a graphic using different tools.
This dataset contains an excerpt of the balance sheet of used _Tesla cars_ sold daily in the United States from tesla.com.


## Tables

 		Customer
 		Employee
 		Orders
 		Sales fact table
 		Tesl_used_car_sold
 		Transaction
		
## Data Model

	Logical Data Model (Visual paradigm Enterprise) <https://github.com/yahya-demo-user/SATURN-DATA/blob/ae3a8dfa0fdd5714a6a9761688e89fd0ea115123/Data%20model/Logical%20Data%20Model.vpp>
	Physical Data Model (Visual paradigm Enterprise)
	
## Tools

 		- Visual paradigm Enterprise (Logical Data Model + Physical Data Model).
 		- DBeaver (Upload Data).
 		- Amazon Aurora Provisioned (Compatible with PostgreSQL).
 		- AWS DMS (Used to migrate data from your RDS SQL Server Standard Ed. DB instance to the RDS Aurora (provisioned) DB instance).
 		- Amazon Aurora Serverless (Query Data in the console).
 		- Pycharm Cummunity Edition (Python Boto3) : Connect to the Aurora (serverless) DB instance and run a query.
 		- Kinesis Data Flows (Firehouse) : Created and move Data by the Python/Boto3 script in S3 bucket.
 		- AWS Glue
 		- AWS Athena
 		- AWS Lake Formation
		- Redshift
		- Jupyter
 		- visualizer tool (Tableau)

## Codes

Boto3 code in Python to connect to the Aurora (serverless) DB instance, run and show a query results and code in snapshot.

```
import boto3
import json
from datetime import datetime as dt


# """Works only with Aurora serverless clusters - Must have Data API enabled"""
rds_data = boto3.client('rds-data')
firehose = boto3.client('firehose')
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
    record_batch.append(record_to_stream)

print(record_batch)
batch_response = firehose.put_record_batch(
    DeliveryStreamName='facttable',
    Records=record_batch
)

print(batch_response)
```

![image](https://user-images.githubusercontent.com/112673539/227347426-c81443c5-ce7d-461c-9a6c-71f03ecc103e.png)

Modify your Python/Boto3 code to connect to the Firehose Delivery Stream / Run code and show result

![image](https://user-images.githubusercontent.com/112673539/227348274-7dfbdc45-2e2d-4925-935b-b3eaaa75689d.png)

 Make a copy of your Python/Boto3 script. In the copy, change the Kinesis connection from Firehose to the new Data Stream.
 
 ```
import boto3
import json
from datetime import datetime as dt


# """Works only with Aurora serverless clusters - Must have Data API enabled"""
rds_data = boto3.client('rds-data')
kinesis = boto3.client('kinesis')
query = """
        select * from dbo.orders;
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
columns = ['order_number', 'first_name', 'Last_name', 'customer_id', 'Employee_id']

shard_data = kinesis.list_shards(
    StreamName='transactionnew'
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
    StreamName='transactionnew'
)

print(kinesis_response)

```

![image](https://user-images.githubusercontent.com/112673539/227348804-86000699-8498-4b36-a776-0c225627064f.png)

## Analytics diagram

![image](https://user-images.githubusercontent.com/112673539/227622192-1d871559-7993-4980-a282-a3bb1030f371.png)

## Authors

	@Yahya houti

## License

	MIT © Yahya Houti

## Acknowledgments

Big thanks to 

$${\color{blue}Southeast \space \color{blue}Community \space \color{blue}College}$$
<p align="center">For this very rewarding program.


$${\color{blue}Joe \space \color{blue}Cobarrubias \space \color{black}and  \space \color{blue}Jeremy \space \color{blue}Skog}$$
<p align="center">For all the support, follow-up and efforts they have provided for the deployment of this program.

