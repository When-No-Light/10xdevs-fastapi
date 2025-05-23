"""Script to generate OpenApi schema (for FastAPI app) and write it to
'/src/javascript/Fast-api-test/.openapi_schemas'.

This schema needed to generate client to connect wih api.'
"""
import json
from pathlib import Path

from public_reports_service.main import app


def generate_schema():
    """Generate and put openapi schema to `js_project_dir`."""
    current_file_directory = Path.cwd()
    js_project_dir = f"{current_file_directory}/src/javascript/Fast-api-test"

    # define folder to write openapi schema
    openapi_schemas_dir = f"{js_project_dir}/.openapi_schemas"
    Path(openapi_schemas_dir).mkdir(parents=True, exist_ok=True)

    file_path = Path(f"{openapi_schemas_dir}/fast_api_test.json")

    # get schema from fastapi app
    # this object knows everything about the implemented methods
    openapi_content = app.openapi()

    # ref. openapi schema to make TS classes that we want to generate in the next steps more readable
    # if you need more information, I have left a link to the documentation page
    # # https://fastapi.tiangolo.com/advanced/generate-clients/#__tabbed_4_1
    for path_data in openapi_content["paths"].values():
        for operation in path_data.values():
            tag = operation["tags"][0]
            operation_id = operation["operationId"]
            to_remove = f"{tag}-"
            new_operation_id = operation_id[len(to_remove) :]
            operation["operationId"] = new_operation_id

    # write schema to file in quasar project dir
    file_path.write_text(json.dumps(openapi_content), encoding="utf-8")


if __name__ == "__main__":
    generate_schema()
