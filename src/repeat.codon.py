from bio import *

LIBDIVSUFSORT="lib/libdivsufsort.so.3"
from C import LIBDIVSUFSORT.divsufsort(ptr[byte], Ptr[Int[32]], int)

def main():
    Text = "abracadabra"
    n = len(Text)
    SA = Ptr[Int[32]](n)
    divsufsort(Text.c_str(), SA, n)

    for i in range(n):
        print(f'SA[{i}] = {SA[i]}')


main()
