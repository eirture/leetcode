
PWD:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: commit
commit: table
	./scripts/commit.sh


.PHONY: table
table:
	@git add -A
	@./scripts/updatetables.py

.PHONY: new
new:
	./scripts/fetch-leetcode.py ${url} -o ${PWD}/algorithms 