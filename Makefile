.PHONY: help kitchen kitchen-create kitchen-converge kitchen-verify kitchen-test kitchen-list clean ci-add ci-merge-ff ci-merge
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

kitchen: kitchen-check kitchen-create kitchen-converge kitchen-verify kitchen-list ## kitchen check,create,converge,verify,list

kitchen-create: kitchen-check
	kitchen create

kitchen-converge: kitchen-check
	kitchen converge

kitchen-verify: kitchen-check
	! [ -d ./tests/integration ] || kitchen verify -t tests/integration
	[ -d ./tests/integration ]   || kitchen verify

kitchen-test: kitchen-check
	! [ -d ./tests/integration ] || kitchen test -t tests/integration
	[ -d ./tests/integration ]   || kitchen test

kitchen-list: kitchen-check ## kitchen list
	kitchen list

clean: ## cleanup dir
	! [ -x "$(shell which kitchen)" ] || kitchen destroy
	! [ -d ./.kitchen ] || rm -rf ./.kitchen

ci-add:
	bash ci/add_pipeline.sh

ci-merge-ff:
	bash ci/trigger-merge-ff.sh

ci-merge: ci-merge-ff
