submodules:
	git submodule update --init

libdivsufsort:
	mkdir -p extern/libdivsufsort/build
	cd extern/libdivsufsort/build && \
	cmake \
		-DCMAKE_BUILD_TYPE="Release" \
		-DCMAKE_INSTALL_PREFIX="../../.." .. && \
	make && \
	sudo make install

example:
	export LD_LIBRARY_PATH=./lib:$LD_LIBRARY_PATH
	gcc src/example.c -Wall -I ./include -o bin/example.out -Llib -ldivsufsort

clean:
	rm -rf extern/libdivsufsort/build bin/*.out lib/*

rdi:
	codon build -plugin seq src/repeat.codon.py -o bin/rdi

btree:
	~/.codon/bin/codon run -plugin seq src/btree.codon.py

home:
	echo $(HOME)
