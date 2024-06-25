from backend.database.test_db_manage import TestDBManage
import json
import backend.config.configs as configs

DB_NAME=configs.DB_NAME
def get_server_list():
    with TestDBManage(DB_NAME) as db_manager:
        servers = db_manager.get_all_server()
    server_list = [item['serverName'] for item in servers]
    return server_list


def get_api_url_by_server(server_name):
    with TestDBManage(DB_NAME) as db_manager:
        api_url_list = db_manager.get_apiUrl_by_server(server_name=server_name)
    return api_url_list


def get_api_request_response(server_name, api_url, method):
    if not server_name or not api_url or not method:
        result = {}
        result["request"] = json.dumps({
            "Info": "Server_name, api_url, and method must not be empty or None"})
        result["response"] = json.dumps({
            "Info": "No response"})
        return result
    with TestDBManage(DB_NAME) as db_manager:
        rs = db_manager.get_api_request_response(
            server=server_name, api_url=api_url, method=method)
    if "request" not in rs or rs["request"] is None:
        rs["request"] = json.dumps({"Info": "no request"})
    if "response" not in rs or rs["response"] is None:
        rs["response"] = json.dumps({"Info": "no response"})
    return rs


def get_api_details(server_name, api_url, method):
    rs = get_api_request_response(server_name, api_url, method)
    details = {}
    details["request"] = json.loads(rs["request"])
    details["response"] = json.loads(rs["response"])
    return details["request"], details["response"]


def get_method_list(server_name, api_url):
    with TestDBManage(DB_NAME) as db_manager:
        method_list = db_manager.get_method_by_url(
            server_name=server_name, url=api_url)
    return method_list
