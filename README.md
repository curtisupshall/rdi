# rd-index

## 0. Prerequisites
 - [Codon](https://docs.exaloop.io/codon/) and [Seq](https://docs.seq-lang.org/):

```bash
bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
export platform=$(uname -s | awk '{print tolower($0)}')-$(uname -m)
curl -L https://github.com/exaloop/seq/releases/download/v0.11.3/seq-${platform}.tar.gz \
| tar zxvf - -C ˜/.codon/lib/codon/plugins
```

 - CMake:
 
```bash
sudo apt install cmake
```

## 1. Setup
 0. Clone the repo: `git clone git@github.com:curtisupshall/rd-index`
 1. Fetch submodules: `make submodules`
 2. Install libdivsufsort: `make libdivsufsort`

## 2. Running the Program
```bash
make rd-index
```
