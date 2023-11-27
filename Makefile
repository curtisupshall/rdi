libdivsufsort:
	mkdir -p extern/libdivsufsort/build
	cd extern/libdivsufsort/build && \
	cmake -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX="../../.." .. && \
	make && \
	sudo make install

example:
	gcc src/example.c -Wall -I ./include -o bin/example

clean:
	rm -rf extern/libdivsufsort/build
