help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	npm install nodemon
	pip install -r requirements.txt

python: ## Format Python
	./py2.py "README.md" > /tmp/newstyle.md
	mv /tmp/newstyle.md "README.md"

watch:
	./node_modules/.bin/nodemon --exec "$(MAKE) python" --ext md,cfg,py --delay 5
