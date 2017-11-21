from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DECIMAL
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
    partner_id = Column(Integer, ForeignKey(Partner.id), nullable=False)
    partner = relationship(Partner, innerjoin=True)


class Subsidiary(Base):
    __tablename__ = 'DimFilial'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    region_id = Column(Integer, ForeignKey(Region.id), nullable=False)
    region = relationship(Region, innerjoin=True)


class Transaction(Base):
    __tablename__ = 'DimFatoExtrato'
    id = Column(Integer, primary_key=True)
    subsidiary_id = Column(Integer, ForeignKey(Subsidiary.id), nullable=False)
    subsidiary = relationship(Subsidiary, innerjoin=True)
    sale = Column(DECIMAL(2));
    pointz_sale = Column(DECIMAL(2));
    pointz = Column(Integer, nullable=False)


if __name__ == '__main__':
    engine = create_engine(
        "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
    )

    Base.metadata.create_all(engine)
