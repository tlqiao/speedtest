from backend.database.test_db_manage import TestDBManage
import backend.config.configs as configs
from backend.apitest.parse_swagger import parse_swagger_file


def import_swagger_file(server_name, file):
    api_info_list = parse_swagger_file(file_path=file.name)
    with TestDBManage(configs.DB_NAME) as db_manager:
        db_manager.update_apiInfo_document(server_name, api_info_list)
    return f" Import Swagger File Successfully"


def add_server(server_name):
    if not server_name:
        return "Server_name must not be empty or None."
    with TestDBManage(configs.DB_NAME) as db_manager:
        db_manager.add_server(server_name)
        return "Add server successfully"


def manual_import_apiInfo(server_name, api_url, method, request, response):
    if not server_name or not api_url or not method:
        return "Server_name, api_url, and method must not be empty or None."
    with TestDBManage(configs.DB_NAME) as db_manager:
        db_manager.update_api_info(
            server_name, api_url=api_url, method=method, request=request, response=response)
    return "Manually Import API Details Successful"

def add_api_url(server_name, api_url, method):
    if not server_name or not api_url or not method:
        return "Server_name, api_url, and method must not be empty or None."
    with TestDBManage(configs.DB_NAME) as db_manager:
        db_manager.add_apiUrl(server_name=server_name,
                              api_url=api_url, method=method)
        return "Add api url successfully"

