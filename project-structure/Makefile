# https://docs.aws.amazon.com/pt_br/lambda/latest/dg/python-package.html

init:
	python3 -m venv venv; source venv/bin/activate; pip install -r requirements.txt

test: init
	coverage run -m unittest discover -s ./src/test/python -p '*_test.py'
	coverage report -m

clean_cache:
	# Foi preciso escapar o $ para o make não interpretar como uma variável
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

package_dependencies:
	cd venv/lib/python3.*/site-packages; zip -r9 ../../../../function.zip . 2>/dev/null || :

package: init test clean_cache package_dependencies
	mkdir -p deploy/src/main/
	cp -R src/main/* deploy/src/main/
	cd deploy/; zip -r ../function.zip .
	rm -rf deploy