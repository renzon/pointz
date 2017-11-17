from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Partner(Base):
    __tablename__ = 'DimParceiro'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    segment = Column(String(60), nullable=False)


class Region(Base):
    __tablename__ = 'DimHierarquiaRegional'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    partner_id = Column(Integer, ForeignKey('DimParceiro.id'), nullable=False)
    partner = relationship(Partner, innerjoin=True)


engine = create_engine(
    "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
)

Base.metadata.create_all(engine)
