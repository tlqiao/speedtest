import re
from backend.database.data_db_manage import DataDBManage
import backend.config.configs as configs

def extract_mysql_schema_file(file_path):
    tables = {}
    current_table_name = None
    current_table_sql = ""

    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("CREATE TABLE"):
                match = re.match(r"CREATE TABLE `(.*)`", line)
                if match:
                    current_table_name = match.group(1)
                    current_table_sql = line
            elif re.match(r"\) ENGINE=.*;", line):
                current_table_sql += line
                if current_table_name and current_table_sql:
                    tables[current_table_name] = current_table_sql
                    current_table_name = None
                    current_table_sql = ""
            elif current_table_sql:
                current_table_sql += line

    return tables

def import_mysql_tables(db_type,db_name,file_path):
    tables=extract_mysql_schema_file(file_path=file_path)
    with DataDBManage(configs.DB_NAME) as data_db_manage:
        for table_name,create_table_sql in tables.items():
           data_db_manage.add_table(
              db_type=db_type,db_name=db_name, table_name=table_name, table_schema=create_table_sql)
    return"import table schema file successfully"       
           
def get_table_schema(db_name, table_list):
    rs=""
    with DataDBManage(configs.DB_NAME) as data_db_manage:
        for item in table_list:
            rs = rs+data_db_manage.get_table_schema(db_name, item)+'\n'
    return rs    

def add_database(db_name):
    with DataDBManage(configs.DB_NAME) as data_db_manage:
        data_db_manage.add_database(db_name=db_name)
    return "Add DB Successfully"


def get_all_database():
    with DataDBManage(configs.DB_NAME) as data_db_manage:
        db_list = data_db_manage.get_all_database()
    return db_list


def get_all_tables(db_name):
    with DataDBManage(configs.DB_NAME) as data_db_manage:
        table_list = data_db_manage.get_tables(db_name=db_name)
    return table_list




