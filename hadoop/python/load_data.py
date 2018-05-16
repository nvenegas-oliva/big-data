import pandas as pd
from sqlalchemy import create_engine
import psycopg2

donations = pd.read_csv("~/github/big-data/data/opendata/partial_donations.csv")
url = "https://raw.githubusercontent.com/nicomak/blog/master/donors/src/main/resources/opendata_donations_sample.csv"
head = pd.read_csv(url)

## Add columns name from head dataset
donations.columns = head.columns
engine = create_engine('postgresql://nicolas:000@localhost:5432/opendata')

## Create table in opendata database
donations.to_sql("donations", engine)