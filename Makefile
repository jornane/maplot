maplot: plot.py
	rm -rf maplot
	mkdir maplot
	pip3 install -r requirements.txt -t ./maplot/
	rmdir maplot || true
	cp plot.py maplot/
