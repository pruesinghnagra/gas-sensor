.PHONY: test clean

test:
	python3 test_gas_sensor.py

clean:
	rm -rf __pycache__
	rm -f *.pyc
