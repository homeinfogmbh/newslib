FILE_LIST = ./.installed_files.txt

.PHONY: pull push clean generate-bindings install uninstall

default: | clean pull generate-bindings install

generate-bindings:
	@ pyxbgen -u news.xsd -m dom --module-prefix=newslib

install:
	@ ./setup.py install --record $(FILE_LIST)

uninstall:
	@ while read FILE; do echo "Removing: $$FILE"; rm "$$FILE"; done < $(FILE_LIST)

clean:
	@ rm -Rf ./build
	@ rm -f newslib/dom.py

pull:
	@ git pull

push:
	@ git push
