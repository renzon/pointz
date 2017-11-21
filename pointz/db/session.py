from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=create_engine(
    "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
))