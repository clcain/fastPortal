build:
	rm -rf ./html/*
	cp -r ./static/* ./html/
	@for i in `ls portals/`; do \
		bname=$$(basename $$i); \
		name=$${bname%.*}; \
		echo "$$bname -> $${name}.html"; \
		./fastPortal.py ./portals/$$bname ./html/$${name}.html; \
	done

env:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

up: down build
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

clean: rm
	docker-compose down -t 0
	docker-compose rm -fv
	rm -rf ./html/*

.PHONY: *
