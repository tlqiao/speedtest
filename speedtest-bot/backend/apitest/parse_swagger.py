import random
import uuid
from datetime import date
import string
import json


# def find_schemas_without_ref(swagger_components):
#     result = {}
#     schemas = swagger_components.get("schemas", {})
#     for schema_name, schema_definition in schemas.items():
#         if not has_ref_in_schema(schema_definition):
#             result[schema_name] = schema_definition
#     return result


def replace_refs_with_real_object(swagger_data, numbers):
    schemas = swagger_data

    def replace_refs(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref_path = obj["$ref"]
                ref_path = ref_path.split("/")
                ref_path = ref_path[numbers:]  # Remove "#/components/schemas/"
                real_object = schemas
                for part in ref_path:
                    real_object = real_object.get(part, {})
                return real_object
            else:
                for key, value in obj.items():
                    obj[key] = replace_refs(value)
                if "anyOf" in obj:
                    for i, item in enumerate(obj["anyOf"]):
                        obj["anyOf"][i] = replace_refs(item)
                if "items" in obj:
                    obj["items"] = replace_refs(obj["items"])
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                obj[i] = replace_refs(item)
        return obj

    for schema_name in schemas:
        schemas[schema_name] = replace_refs(schemas[schema_name])
    return swagger_data


# def has_ref_in_schema(schema_definition):
#     if "$ref" in schema_definition:
#         return True

#     if "allOf" in schema_definition:
#         for sub_schema in schema_definition.get("allOf", []):
#             if has_ref_in_schema(sub_schema):
#                 return True

#     for key, value in schema_definition.items():
#         if isinstance(value, dict) and has_ref_in_schema(value):
#             return True

#     return False


def replace_components(swagger_data):
    return replace_refs_with_real_object(
        swagger_data["components"]["schemas"], 3)


def replace_api_ref(swagger_data):
    return replace_refs_with_real_object(swagger_data, 1)


def read_swagger_file(swagger_file_path):
    try:
        with open(swagger_file_path, 'r') as file:
            swagger_data = json.load(file)
        return swagger_data
    except FileNotFoundError:
        print(f"Swagger file '{swagger_file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def replace_ref_in_swagger(swagger_file_path):
    swagger_data = read_swagger_file(swagger_file_path)
    new_swagger_data = swagger_data
    update_component_data = replace_components(swagger_data)
    new_swagger_data["components"]["schemas"] = update_component_data
    latest_swagger_data = replace_api_ref(new_swagger_data)
    return latest_swagger_data


def is_valid_http_method(method):
    valid_methods = ["GET", "POST", "PUT", "DELETE"]
    return method.upper() in valid_methods


def extract_api_info(swagger_data):
    api_list = []
    for path, methods in swagger_data.get("paths", {}).items():
        for method, method_info in methods.items():
            if is_valid_http_method(method=method):
                api_info = {
                    "url": path,
                    "method": method,
                    "request": None,
                    "response": None,
                }
                if "requestBody" in method_info:
                    api_info["request"] = method_info["requestBody"]
                if "responses" in method_info:
                    api_info["response"] = method_info.get("responses")
                api_list.append(api_info)

    return api_list


def parse_swagger_file(file_path):
    swagger_data = replace_ref_in_swagger(file_path)
    return extract_api_info(swagger_data)

# def generate_object_properties(schema):
#     new_object = {}
#     for prop, prop_info in schema['properties'].items():
#         prop_type = prop_info['type']
#         prop_format = prop_info.get('format', None)

#         if "enum" in prop_info:
#             new_object[prop] = random.choice(prop_info["enum"])
#         elif prop_type == "string":
#             if prop_format == "uuid":
#                 new_object[prop] = str(uuid.uuid4())
#             elif prop_format == "date":
#                 new_object[prop] = date.today().isoformat()
#             else:
#                 # Generate a random string of length between 1 and 10
#                 new_object[prop] = ''.join(random.choice(
#                     string.ascii_letters) for _ in range(random.randint(1, 10)))
#         elif prop_type == "number":
#             if prop_format == "double":
#                 new_object[prop] = random.uniform(0, 1)
#             else:
#                 new_object[prop] = random.randint(0, 100)
#         elif prop_type == "integer":
#             new_object[prop] = random.randint(0, 100)
#         elif prop_type == "boolean":
#             new_object[prop] = random.choice([True, False])
#     return new_object
