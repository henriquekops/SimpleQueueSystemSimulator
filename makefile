venv:
	python3 -m venv venv
	pip3 install -r requirements.txt

activate:
	source venv/bin/activate

run:
	python3 main.py
