
PWD:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: commit
commit:
	./scripts/commit.sh


.PHONY: table
table:
	@./scripts/updatetables.py
	git add README.md
	git commit -m 'update the table'

.PHONY: new
new:
	./scripts/fetch-leetcode.py ${url} -o ${PWD}/algorithms 