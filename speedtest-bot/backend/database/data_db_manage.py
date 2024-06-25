import pymongo
from backend.database.base_db_manage import BaseDBManage


class DataDBManage(BaseDBManage):
    def add_database(self, db_name):
        database_collection = self.db["database"]
        existing_db = database_collection.find_one(
            {"db_name": db_name})
        if existing_db:
            print(f'database "{db_name}" exist, do not need to added')
        else:
            database_collection.insert_one({"db_name": db_name})
            print(f'add database:  "{db_name}" successfully')

    def add_table(self, db_type,db_name, table_name, table_schema):
        table_collection = self.db["table_info"]
        query = {"db_type":db_type,
            "db_name": db_name,
                 "table_name": table_name}
        update_data = {
            "$set": {
                "table_schema": table_schema
            }
        }
        result = table_collection.update_one(query, update_data, upsert=True)
        if result.upserted_id:
            print(f"Inserted table schema with ID: {result.upserted_id}")
        else:
            print(f"Updated table schema with ID: {result.modified_count}")

    def get_all_database(self):
        database_collection = self.db["database"]
        result = database_collection.find({}, {"_id": 0, "db_name": 1})
        db_names = [db["db_name"] for db in result]
        return db_names

    def get_tables(self, db_name):
        table_collection = self.db["table_info"]
        result = table_collection.find({"db_name": db_name})
        table_name_list = [document["table_name"] for document in result]
        return table_name_list

    def get_table_schema(self, db_name, table_name):
        table_collection = self.db["table_info"]
        query = {"db_name": db_name, "table_name": table_name}
        result = table_collection.find_one(query)
        return result["table_schema"] if result is not None else "no result"
