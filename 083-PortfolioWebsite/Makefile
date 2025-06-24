# Define variables
VUE_DIR = site
STATIC_DIR = static/portfolio-site

# Build Vue app and copy static files to Flask project
build:
	cd $(VUE_DIR) && npm run build
	mkdir -p $(STATIC_DIR)
	cp -r $(VUE_DIR)/dist/* $(STATIC_DIR)/

.PHONY: web
web:
	cd $(VUE_DIR) && npm run dev -- --host 0.0.0.0

dbadmin:
	sqlite_web instance/projects.db

