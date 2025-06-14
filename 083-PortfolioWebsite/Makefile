# Define variables
VUE_DIR = portfolio-site
STATIC_DIR = static/portfolio-site

# Build Vue app and copy static files to Flask project
build:
	cd $(VUE_DIR) && npm run build
	mkdir -p $(STATIC_DIR)
	cp -r $(VUE_DIR)/dist/* $(STATIC_DIR)/

server:
	cd $(VUE_DIR) && npm run dev