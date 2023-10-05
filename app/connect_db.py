from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:mysecretpassword@127.0.0.1:5433/postgres")
Session = sessionmaker(bind=engine)
session = Session()