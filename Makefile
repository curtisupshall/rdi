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

clean:
	rm -rf rdi data/*.rdi .rdilist

rdi:
	codon build -release -plugin seq src/rdi.codon -o rdi

dev:
	codon build -plugin seq src/rdi.codon -o rdi

assembly:
	./rdi assembly data/SRR15652545.fastq --lmin 14 --lmax 18 -a 200 -c 2929

btree:
	codon run -plugin seq src/btree.codon

all: submodules libdivsufsort rdi

.PHONY: submodules libdivsufsort clean rdi btree
