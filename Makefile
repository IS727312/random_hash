install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-aws:
	pip install --upgrade pip &&\
		pip install -r requirements-aws.txt

install-amazon-linux:
	pip install --upgrade pip &&\
		pip install -r amazon-linux.txt
lint:
	pylint --disable=R,C hello.py

format: 
	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py