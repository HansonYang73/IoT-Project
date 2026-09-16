from sqlalchemy import create_engine, MetaData, inspect, delete, text, update, select

class Db():
    instance = None
    def __init__(self):
        ...
    def get_instance():
        if Db.instance == None:
            ...
            
        
