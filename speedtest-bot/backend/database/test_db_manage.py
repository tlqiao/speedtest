import json
from backend.database.base_db_manage import BaseDBManage


class TestDBManage(BaseDBManage):

    def add_server(self, server_names):
        server_collection = self.db["servers"]
        if isinstance(server_names, str):
            obj = {}
            obj["serverName"] = server_names
            server_names = [obj]
        for server_name in server_names:
            existing_server = server_collection.find_one(
                {"serverName": server_name})
            if existing_server:
                print(f'服务器 "{server_name}" 已存在，不进行添加')
            else:
                server_document = {"serverName": server_name}
                result = server_collection.insert_one(server_document)
                print(f'服务器 "{server_name}" 已成功添加')

    def add_apiUrl(self, server_name, api_url, method):
        apiInfo_collection = self.db["api_info"]
        query = {"server": server_name, "api_url": api_url, "method": method}
        result = apiInfo_collection.find_one(query)
        if result:
            print(f'api url has exist')
        else:
            document = {"server": server_name, "api_url": api_url,
                        "method": method, "request": None, "response": None}
            apiInfo_collection.insert_one(document)
            print(f'Has add api_url successfully')

    def get_all_server(self):
        server_collection = self.db["servers"]
        result = server_collection.find({}, {"_id": 0, "serverName": 1})
        server_names = [server["serverName"] for server in result]
        return server_names

    def get_web_pages_by_server(self, server_name):
        uiInfo_collection = self.db["ui_info"]
        result = uiInfo_collection.find({"server_name": server_name})
        page_name_list = [document["page_name"] for document in result]
        return page_name_list

    def get_web_locators_by_page(self, server_name, tool, page_name):
        uiInfo_collection = self.db["ui_info"]
        query = {"server_name": server_name,
                 "tool": tool, "page_name": page_name}
        result = uiInfo_collection.find_one(query)
        return result["locators"]

    def add_web_page(self, server_name, tool, page_name):
        uiInfo_collection = self.db["ui_info"]
        query = {"server_name": server_name,
                 "tool": tool, "page_name": page_name}
        result = uiInfo_collection.find_one(query)
        if result:
            print("Page has existed")
        else:
            uiInfo_collection.insert_one({
                "server_name": server_name,
                "tool": tool,
                "page_name": page_name,
                "locators": None
            })

    def update_web_ui_locators(self, server_name, page_name, tool, locators):
        collection = self.db["ui_info"]
        query = {"server_name": server_name,
                 "page_name": page_name,
                 "tool": tool}
        update_data = {
            "$set": {
                "locators": locators
            }
        }
        result = collection.update_one(query, update_data, upsert=True)
        if result.upserted_id:
            print(f"Inserted new document with ID: {result.upserted_id}")
        else:
            print(f"Updated document with ID: {result.modified_count}")

    def add_mobile_page(self, server_name, tool, platform, page_name):
        mobileInfo_collection = self.db["mobile_info"]
        query = {"server_name": server_name,
                 "tool": tool, "platform": platform, "page_name": page_name}
        result = mobileInfo_collection.find_one(query)
        if result:
            print("Page has existed")
        else:
            mobileInfo_collection.insert_one({
                "server_name": server_name,
                "tool": tool,
                "platform": platform,
                "page_name": page_name,
                "locators": None
            })

    def get_mobile_pages_by_server(self, server_name):
        uiInfo_collection = self.db["mobile_info"]
        result = uiInfo_collection.find({"server_name": server_name})
        page_name_list = [document["page_name"] for document in result]
        return page_name_list

    def get_mobile_locators_by_page(self, server_name, tool, platform, page_name):
        uiInfo_collection = self.db["mobile_info"]
        query = {"server_name": server_name,
                 "tool": tool,
                 "platform": platform,
                 "page_name": page_name}
        result = uiInfo_collection.find_one(query)
        return result["locators"]

    def update_mobile_ui_locators(self, server_name, page_name, tool, platform, locators):
        collection = self.db["mobile_info"]
        query = {"server_name": server_name,
                 "page_name": page_name,
                 "tool": tool,
                 "platform": platform}
        update_data = {
            "$set": {
                "locators": locators
            }
        }
        result = collection.update_one(query, update_data, upsert=True)
        if result.upserted_id:
            print(f"Inserted new document with ID: {result.upserted_id}")
        else:
            print(f"Updated document with ID: {result.modified_count}")

    def add_mobile_page(self, server_name, tool, platform, page_name):
        uiInfo_collection = self.db["mobile_info"]
        query = {"server_name": server_name,
                 "tool": tool, "platform": platform, "page_name": page_name}
        result = uiInfo_collection.find_one(query)
        if result:
            print("Page has existed")
        else:
            uiInfo_collection.insert_one({
                "server_name": server_name,
                "tool": tool,
                "platform": platform,
                "page_name": page_name,
                "locators": None
            })

    def get_apiUrl_by_server(self, server_name):
        apiInfo_collection = self.db["api_info"]
        result = apiInfo_collection.find({"server": server_name})
        api_url_list = [document["api_url"] for document in result]
        return api_url_list

    def get_method_by_url(self, server_name, url):
        apiInfo_collection = self.db["api_info"]
        result = apiInfo_collection.find(
            {"server": server_name, "api_url": url})
        method_list = [document["method"] for document in result]
        return method_list

    def get_api_request_response(self, server, api_url, method):
        apiInfo_collection = self.db["api_info"]
        result = apiInfo_collection.find(
            {"server": server, "api_url": api_url, "method": method}).limit(1).next()
        return result

    def update_apiInfo_document(self, server_name, documents):
        collection = self.db["api_info"]
        for document in documents:
            query = {
                "api_url": document["url"],
                "method": document["method"].upper(),
                "server": server_name
            }
            update_data = {
                "$set": {
                    "request": json.dumps(document["request"]),
                    "response": json.dumps(document["response"])
                }
            }
            result = collection.update_one(query, update_data, upsert=True)
            if result.upserted_id:
                print(f"Inserted new document with ID: {result.upserted_id}")
            else:
                print(f"Updated document with ID: {result.modified_count}")

    def update_api_info(self, server_name, api_url, method, request, response):
        apiInfo_collection = self.db["api_info"]
        query = {
            "server": server_name,
            "method": method.upper(),
            "api_url": api_url
        }
        update = {
            "$set": {
                "request": request,
                "response": response
            }
        }
        result = apiInfo_collection.update_one(query, update, upsert=True)
        if result.upserted_id:
            print(f"Inserted new document with ID: {result.upserted_id}")
        else:
            print(f"Updated document with ID: {result.modified_count}")

    def add_persist_path(self, persist_path):
        collection = self.db["persist_path"]
        path_exist = collection.find_one(
            {"persist_path": persist_path})
        if path_exist:
            print(f'Persist path "{persist_path}" exist, do not need to added')
        else:
            collection.insert_one({"persist_path": persist_path})
            print(f'add persist_path:  "{persist_path}" successfully')

    def add_document_info(self,dest_file_path, file_name, vector_path, persist_path):
        collection = self.db["document_info"]
        query = {"persist_path": persist_path,
                 "file_name": file_name}
        update_data = {
            "$set": {
                "dest_file_path": dest_file_path,
                "file_name": file_name,
                "vector_path": vector_path,
                "persist_path": persist_path}
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
