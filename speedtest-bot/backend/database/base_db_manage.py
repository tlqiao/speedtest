import pymongo
import backend.config.configs as configs

class BaseDBManage:
    def __init__(self, database_name):
        self.database_name = database_name

    def __enter__(self):
        self.client = pymongo.MongoClient(configs.DB_URL)
        self.db = self.client[self.database_name]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def save_document(self, collection_name, documents):
        collection = self.db[collection_name]
        collection.insert_many(documents)

    def clear_data(self, collection_name):
        self.db[collection_name].drop()