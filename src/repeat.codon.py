from bio import *

LIBDIVSUFSORT="lib/libdivsufsort.so.3"
from C import LIBDIVSUFSORT.divsufsort(ptr[byte], ptr[int], int)



class RDIndex:

    def query(l: int, r: int):
        return None
    

def main():
    Text = "abracadabra"
    n = len(Text)
    SA = Ptr[int](n)

    print(f'n = {n}')

    divsufsort(Text.c_str(), SA, n)

    for i in range(n):
        print(f'SA[{i}] = {SA[i]}')



main()
