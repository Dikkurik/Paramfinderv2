from sqlalchemy import create_engine, insert
from sqlalchemy import Table, String, Integer, Column 
from sqlalchemy.orm import declarative_base

dbengine = create_engine("sqlite:///dbmetrics.db", echo=True)
Base = declarative_base()


# Define tables
class Metrics(Base):
    __tablename__ = "latency"

    id = Column(Integer, primary_key=True)
    page_name = Column(String)
    load_time = Column(Integer)

    def __repr__(self):
        return f"Page: (page_name={self.page_name!r}, load_time={self.load_time!r})"

class Containers(Base):
    __tablename__ = "container_time"

    id = Column(Integer, primary_key=True)
    page_name = Column(String)
    life_time = Column(Integer)

    def __repr__(self):
        return f"Page: (page_name={self.page_name!r}, life_time={self.load_time!r})"

# Operations
def insert_to_metrics(page_name:str, load_time:int):
    query = insert(Metrics).values(page_name=page_name, load_time=load_time)

    with dbengine.connect() as conn:
        res = conn.execute(query)
        Base.metadata.create_all(dbengine)

def insert_to_containers(page_name:str, life_time:int):
    query = insert(Containers).values(page_name=page_name, life_time=life_time)

    with dbengine.connect() as conn:
        res = conn.execute(query)
        Base.metadata.create_all(dbengine)
   

