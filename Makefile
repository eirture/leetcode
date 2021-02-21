
.PHONY: commit
commit:
	./scripts/commit.sh


.PHONY: table
table:
	@./scripts/updatetables.py
