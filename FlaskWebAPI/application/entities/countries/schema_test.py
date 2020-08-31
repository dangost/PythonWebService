from application.entities.countries.schema import get_json_schema

a = get_json_schema()

assert type(a) == dict

