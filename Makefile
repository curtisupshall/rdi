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

test_minimap:
	./extern/minimap2/minimap2 -x ava-pb -t8 data/contigs.fa data/contigs.fa | gzip -1 > contigs.paf.gz

test_miniasm:
	./extern/miniasm/miniasm contigs.paf.gz > contigs.gfa

rdi:
	codon build -release -plugin seq src/rdi.codon -o rdi

dev:
	codon build -plugin seq src/rdi.codon -o rdi

assembly:
	./rdi assembly data/SRR15652545.fastq --lmin 14 --lmax 18 -a 200 -c 2929

jaccard:
	codon run -plugin seq src/jaccard.codon

btree:
	codon run -plugin seq src/btree.codon

all: submodules libdivsufsort rdi kmer

.PHONY: submodules libdivsufsort clean rdi btree
