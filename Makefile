actors.list:
	python3 makeActors.py

wells.list:
	python3 makeWells.py

real.dict: actors.list wells.list
	python3 makeReal.py

real.pdf: real.dict
	python3 dict2dot.py real.dict |neato -T pdf > real.pdf

ideal.dict: actors.list wells.list
	python3 makeIdeal.py

ideal.pdf: ideal.dict
	python3 dict2dot.py ideal.dict |neato -T pdf > ideal.pdf
