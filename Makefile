all:
	make update; make html; make deploy;

update:
	git submodule update --remote --merge

html:
	pelican -o MemphisPython.github.io -s settings.py content

deploy:
	cd MemphisPython.github.io && git add -A && git commit -am "updating" && git push && cd ..
