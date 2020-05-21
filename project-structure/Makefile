init:
	pip3 install --target ./package -r requirements.txt

test:
	python3 -m unittest discover -s ./src/test/python -p '*_test.py'

clean_cache:
	# Foi preciso escapar o $ para o make não interpretar como uma variável
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

package_dependencies:
	cd package; zip -r9 ../function.zip . 2>/dev/null || :

package: init test clean_cache package_dependencies
	mkdir -p deploy/src/main/
	cp -R src/main/* deploy/src/main/
	cd deploy/; zip -r ../function.zip .