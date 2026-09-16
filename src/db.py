from sqlalchemy import create_engine, MetaData, inspect, delete, text, update, select
from flask import abort

DATABASE_URL = "sqlite:///db/SmartStore.db"
DEBUG = True

class Db():
    instance = None
    def __init__(self):
        # Connecting to db
        self.engine = create_engine(DATABASE_URL, echo=DEBUG)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)
        self.inspector = inspect(self.engine)
        
        # Initializing the tables
        self.customers = self.metadata.tables["Customers"]
        self.items = self.metadata.tables["Items"]
        self.membership = self.metadata.tables["Memberships"]
        self.orders = self.metadata.tables["Orders"]
        self.order_history = self.metadata.tables["OrdersHistory"]
        self.sales = self.metadata.tables["Sales"]
        
    def get_instance():
        if Db.instance == None:
            Db.instance = Db()
        return Db.instance
        
    def add_customer(self, name, address, email, phone_number):
        try:
            stmt = self.customers.insert().values( 
                Name=name,
                HomeAddress=address,
                Email=email,
                Number=phone_number,
            )
            
            with self.engine.begin() as conn:
                conn.execute(stmt)
            return 0
        except Exception:
            return 1
