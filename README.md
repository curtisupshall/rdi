<p align="center">
  <img src="assets/logo.png" alt="Rdi"/>
</p>

## Abstract
**Motivation:** In bioinformatics, repeated substring detection is an essential task used in structural
variant analysis, comparative genomics, gene assembly, and others. However, existing methods for
finding repeats can be computationally expensive and may not scale well to large datasets.

**Results:** We present RDI: an algorithm to produce an efficient and scalable index that will
return all strings of length $L$ such that they appear exactly $R$ times on the target sequence $T$
when queried with $L$ and $R$. RDI answers queries in approximately $O(\log n)$ time, where $n$ is
the length of the target sequence. On average, our index files are 3.27:1 compared to sequence
size. Preliminary testing shows thatRDI is able to service 1,000,000 queries in 4.00 seconds 
(for $n = 1,986$).


# 🧬 rdi
Repeat Detection Index is an index for finding repeated substrings.

## 0. Prerequisites
 1. [Codon](https://docs.exaloop.io/codon/) **(with Python >=3.8 interoperability enabled)** and [Seq](https://docs.seq-lang.org/):

```bash
bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
export platform=$(uname -s | awk '{print tolower($0)}')-$(uname -m)
curl -L https://github.com/exaloop/seq/releases/download/v0.11.3/seq-${platform}.tar.gz \
| tar zxvf - -C ˜/.codon/lib/codon/plugins
```

Example for Python interoperability:
```bash
export CODON_PYTHON=/usr/lib/python3.8/config-3.8-x86_64-linux-gnu/libpython3.8.so
```

 2. CMake:

```bash
sudo apt install cmake
```

## 1. Setup
 0. Clone the repo: `git clone git@github.com:curtisupshall/rdi`
 1. Fetch submodules: `make submodules`
 2. Install [libdivsufsort](https://github.com/y-256/libdivsufsort): `make libdivsufsort`
 3. Compile RDI: `make rdi`

## 2. Running the Program
RDI runs in two modes. In `index` mode, RDI builds a repeat detection index and writes it to disk next to your input file. In `query` mode, you can make
queries against the index.

### Index Mode

```bash
./rdi index path/to/your/file.fa
```

### Query Mode

```bash
./rdi query -l 10 -r 6
```

|Name|Type|Description
|----|----|-----------
|`-h`, `--help`| - |Help
|`-r`, `--repeats`|`int`|Repeats
|`-l`, `--length`|`int`|Kmer length

## 3. Future Work
 - Indexing strategy; particularly around [perfect minimal hashing](https://en.wikipedia.org/wiki/Perfect_hash_function)
 - Parallelization
 - Pipelining:
```bash
cat mysequence.fa | rdi index
echo "30 10" | rdi query
```
 - REPL

## 4. References
Many thanks to M. Oguzhan Kulekci of Indiana University, Bloomington, for providing the indexing algorithm used in this project, as well as pseudocode, examples, and general guidance.
