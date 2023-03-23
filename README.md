![RealPython](https://user-images.githubusercontent.com/112673539/226464986-6a17242f-1ae0-430d-b920-2c889d13fac6.JPG)

## Table of Contents

 		. Project Title
 		. Description
 		. Tables
 		. Tools 
		. Codes
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
 		- Tableau

## Codes

Boto3 code in Python to connect to the Aurora (serverless) DB instance, run and show a query results and code in snapshot.

![image](https://user-images.githubusercontent.com/112673539/227347426-c81443c5-ce7d-461c-9a6c-71f03ecc103e.png)

Modify your Python/Boto3 code to connect to the Firehose Delivery Stream / Run code and show result

![image](https://user-images.githubusercontent.com/112673539/227348274-7dfbdc45-2e2d-4925-935b-b3eaaa75689d.png)

 Make a copy of your Python/Boto3 script. In the copy, change the Kinesis connection from Firehose to the new Data Stream.

![image](https://user-images.githubusercontent.com/112673539/227348804-86000699-8498-4b36-a776-0c225627064f.png)


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

