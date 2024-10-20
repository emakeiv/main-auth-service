.PHONY: install
install :
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: format
format :
	black src/*.py tst/*.py