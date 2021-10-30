.PHONY: venv activate run

venv:
	( \
		python3 -m venv venv; \
		. venv/bin/activate; \
		pip3 install -r requirements.txt; \
	)

run:
	python3 main.py;
