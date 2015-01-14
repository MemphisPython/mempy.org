all:
	make update; make html; make deploy;

html:
	pelican -o MemphisPython.github.io -s settings.py content

update:
	git submodule update --remote --merge

deploy:
	cd MemphisPython.github.io && git add -A && git commit -am "updating" && git push && cd ..
