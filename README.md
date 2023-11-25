# Testing SimpleCart
implement simple cart and promotion

# Setup Guide

## Install, create and activate virtualenv
https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Delete pysam==0.22.0
    Hapus terlebih dahulu pysam==0.22.0 yang ada di file requirements.txt
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/6697bfb8-2eb7-48ec-8450-1ff3a14358b1)

## Install requirements
    pip install -r requirements.txt
    Install pada terminal VSCODE
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/9712be65-9bd9-4161-aeb1-ae090fe0b29c)

## create database
create new database, in this case we're using postgresql

      Contoh pada SQL shell
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/f11d42e6-5218-491a-9e33-13988b77ea2c)
  
      pada VS Code
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/ef7b6f86-b287-4191-8c81-75829f8887d1)

## set env variable
create file .env in the root of the folder, and fill with you credential of your database

    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_PORT = ""
    DB_NAME = ""
    FLASK_DEBUG = true

    Contoh pada database yang dibuat pada file .env melalui VSCode
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/a8fdc8d9-6fbf-47f6-92a4-600d32c61420)

## Create table

run `flask create`to create tables from models.

    Contoh Flask Create pada VSCode
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/8311fd92-be66-4108-9b9a-22f8519ae2dc)

## Insert data product

run this query from your db client
```
INSERT INTO public.product (sku,brand,"name",description,price,non_discountable) VALUES
	 ('ABCKM5','ABC','kecap manis ABC 500ml','kecap manis abc 500ml',25000.0,false),
	 ('INDOSKM25','Indofood','Susu kental manis 250ml','Susu kental manis 250ml',15000.0,false),
	 ('LIOML1','Lion','Mamalemon 1000ml ','Mamalemon 1000ml ',21000.0,false),
	 ('INDOBR','Indofood','Bumbu racik','Bumbu racik',2500.0,false),
	 ('ABCS25','ABC','Sambal 250ml','Sambal 250ml',15000.0,false),
	 ('INDOIGS','Indofood','Indomie goreng special','Indomie goreng special',3000.0,false),
	 ('MYRLM1','mayora','le minerale 1000ml','le minerale 1000ml',8000.0,true);
```
    Database yang di panggil dalam SQL Shell
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/331d9cda-6f26-4f25-89af-496a0aeadf85)

## Run the app
to run the web app simply  use

    flask run
    contoh menjalankan pada VScode
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/b5b8a99f-7745-4e52-b1de-66356f14178b)
  
    kemudian klik link http://127.0.0.1:5000
    jika berhasil di jalankan

![image](https://github.com/MFariz1667/TESTING-DAN-QA-PERANGKAT-LUNAK/assets/133950605/081ef6b6-87ad-468a-bc13-ea52825a0f1f)

to access swagger use url `localhost:5000/apidocs`

    contoh menjalankan local host http://127.0.0.1:5000 dalam web
  ![image](https://github.com/MFariz1667/Testing-QA/assets/133950605/b757f477-bb8f-44e8-bcab-6b8d5309e27f)


## Run test
run test

    pytest

check test coverage

    pytest --cov=myproj tests/


## Debt

 - Cart Update
 - Same product validation on cart
 - Unit test
 - Unit test coverage
 - CI setup 

## Tugas Uas 1
Lengkapi test function berikut
https://github.com/agungperdananto/SimpleCart/blob/616785ea52b257a3060ad1656d15254295e73741/test/test_routes.py#L18-L20
