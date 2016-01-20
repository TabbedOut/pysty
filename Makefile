help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	npm install nodemon
	pip install -r requirements.txt

test: ## Run test suite
	py.test -s

.PHONY: README.md
README.md: ## Generate a new readme
	./py2.py "README.md" --force > /tmp/newstyle.md
	mv /tmp/newstyle.md "README.md"

watch:
	./node_modules/.bin/nodemon --exec "$(MAKE) README.md" --ext md,cfg,py --delay 5
