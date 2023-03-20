# SATURN-DATA

![RealPython](https://user-images.githubusercontent.com/112673539/226463555-cd3d3041-5b95-494b-8d03-668ec275cc24.JPG)

-----Table of Contents

Project Title
Description
Tables
Tools 
Authors
License
Acknowledgments

-----Project Title

SATURN DATA

-----Description

This project consist of getting Raw Data ingested into S3 Bucket, analyze and transforme it into a graphic using different tools.
This dataset contains an excerpt of the balance sheet of used Tesla cars sold daily in the United States from tesla.com


-----Tables :

	Customer
	Employee
	Orders
	Sales fact table
	Tesl_used_car_sold
	Transaction
	
-----Tools :

	Visual paradigm Enterprise (Logical Data Model + Physical Data Model).
	DBeaver (Upload Data).
	Amazon Aurora Provisioned (Compatible with PostgreSQL).
	AWS DMS (Used to migrate data from your RDS SQL Server Standard Ed. DB instance to the RDS Aurora (provisioned) DB instance).
	Amazon Aurora Serverless (Query Data in the console).
	Pycharm Cummunity Edition (Python Boto3) : Connect to the Aurora (serverless) DB instance and run a query.
	Kinesis Data Flows (Firehouse) : Created and move Data by the Python/Boto3 script in S3 bucket.
	AWS Lake Formation
	Redshift
	Jupyter
	Tableau

-----Authors

@DomPizzie

-----License

MIT © Yahya Houti

-----Acknowledgments
Inspiration, code snippets, etc.
