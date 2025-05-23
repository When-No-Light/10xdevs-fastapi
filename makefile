generate_openapi_schema:
	@pants run ./src/python/openapi_schema_generator/run_generator.py

generate_client_from_openapi_schema:
	@cd $(CURDIR)/src/javascript/Fast-api-test && npm install && npm run generate-client
	
set_up:  
	@echo "Generating lockfiles..."
	@pants generate-lockfiles ::
	@echo "Exporting resolve..."
	@pants export --export-resolve="['python-default', 'mypy']"
	@echo "Generating OpenAPI schema..."
	@$(MAKE) generate_openapi_schema
	@echo "Generating client from OpenAPI schema..."
	@$(MAKE) generate_client_from_openapi_schema

precommit_check:
	@echo "Formatting..."
	@pants fmt ::
	@echo "Mypy checking..."
	@pants check ::
	@echo "Pylint checking..."
	@pants lint ::

run_backend:
	@pants run src/python/public_reports_service/main.py

run_frontend:
	@cd $(CURDIR)/src/javascript/Fast-api-test && quasar dev
