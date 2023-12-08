build:
	rm -rf ./html/*
	cp -r ./static/* ./html/
	@cd portals && \
		for i in `ls`; do \
			bname=$$(basename $$i); \
			name=$${bname%.*}; \
			echo "$$i -> $${name}.html"; \
			../fastPortal.py $$i ../html/$${name}.html; \
		done

env:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

up: down
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
