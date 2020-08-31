from application.entities.warehouses.schema import get_json_schema

a = get_json_schema()

assert type(a) == dict

