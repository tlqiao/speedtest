import pymongo
from backend.database.base_db_manage import BaseDBManage


class DataDBManage(BaseDBManage):
    def add_persist_path(self, persist_path):
        collection = self.db["persist_path"]
        path_exist = collection.find_one(
            {"persist_path": persist_path})
        if path_exist:
            print(f'Persist path "{persist_path}" exist, do not need to added')
        else:
            collection.insert_one({"persist_path": persist_path})
            print(f'add persist_path:  "{persist_path}" successfully')

    def add_document_info(self, file_path, file_name, vector_path, persist_path, vector_ids):
        collection = self.db["document_info"]
        query = {"persist_path": persist_path,
                 "file_name": file_name}
        update_data = {
            "$set": {
                "file_path": file_path,
                "file_name": file_name,
                "vector_path": vector_path,
                "persist_path": persist_path,
                "vector_ids": vector_ids}
        }
        result = collection.update_one(query, update_data, upsert=True)
        if result.upserted_id:
            print(f"Inserted new document with ID: {result.upserted_id}")
        else:
            print(f"Updated document with ID: {result.modified_count}")

    def get_all_file_path(self,):
        collection = self.db["persist_path"]
        result = collection.find({}, {"_id": 0, "persist_path": 1})
        persist_paths = [path["persist_path"] for path in result]
        return persist_paths

    def get_all_file_name(self, persist_path):
        collection = self.db["document_info"]
        query = {
            "persist_path": persist_path
        }
        result = collection.find(query, {"_id": 0, "file_name": 1})
        file_names = [file_name["file_name"] for file_name in result]
        return file_names
