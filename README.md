![RealPython](https://user-images.githubusercontent.com/112673539/226464986-6a17242f-1ae0-430d-b920-2c889d13fac6.JPG)

## -----Table of Contents-----

#### 		. Project Title
#### 		. Description
#### 		. Tables
#### 		. Tools 
#### 		. Authors
#### 		. License
#### 		. Acknowledgments

## -----Project Title-----

SATURN DATA

## -----Description-----

This project consist of getting **Raw Data** ingested into **S3 Bucket**, analyze and transforme it into a graphic using different tools.
This dataset contains an excerpt of the balance sheet of used _Tesla cars_ sold daily in the United States from tesla.com


## -----Tables-----

#### 		Customer
#### 		Employee
#### 		Orders
#### 		Sales fact table
#### 		Tesl_used_car_sold
#### 		Transaction
	
## -----Tools-----

###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494613-bb7cac19-807f-4171-91d7-4905e212f871.png) Visual paradigm Enterprise (Logical Data Model + Physical Data Model).
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494671-380bc581-0f72-4bf4-ac57-65c7e52ca24f.png) DBeaver (Upload Data).
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494765-2eaee75c-a352-41f0-889c-1d16441fd3bc.png) Amazon Aurora Provisioned (Compatible with PostgreSQL).
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226493557-ec7c386d-a6f8-4d7a-aebf-38cef6e17c5b.png) AWS DMS (Used to migrate data from your RDS SQL Server Standard Ed. DB instance to the RDS Aurora (provisioned) DB instance).
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494802-e2bd0a87-79c8-426a-8711-d97afbdc8b81.png) Amazon Aurora Serverless (Query Data in the console).
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494947-af14d2e5-4e26-4844-931c-5cc6f928f60a.png) Pycharm Cummunity Edition (Python Boto3) : Connect to the Aurora (serverless) DB instance and run a query.
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226493356-d6738f51-0f53-45d1-8367-42f4be8c0228.png) Kinesis Data Flows (Firehouse) : Created and move Data by the Python/Boto3 script in S3 bucket.
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226493294-e33b3b08-9007-4bcd-bc0a-3cb448551bdc.png) AWS Glue
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226493042-9f24965e-da5b-443b-a8d9-94357198412e.png) AWS Athena
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494502-b142e167-8d32-4731-846d-5e4784c525f3.png) AWS Lake Formation
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226493419-3bcdcb6e-c2fd-4181-917a-644fd3bd1a19.png) Redshift
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494112-e3033e61-05b1-41bb-93aa-89c0f8d18d53.png) Jupyter
###### 		- ![image](https://user-images.githubusercontent.com/112673539/226494313-8c939db9-2374-40e7-a054-7fcac2256651.png) Tableau

## -----Authors-----

	@DomPizzie

## -----License-----

	MIT © Yahya Houti

## -----Acknowledgments-----
	Inspiration, code snippets, etc.
