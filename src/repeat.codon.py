from bio import *

LIBDIVSUFSORT="lib/libdivsufsort.so.3"
from C import LIBDIVSUFSORT.divsufsort(ptr[byte], Ptr[Int[32]], int)

# Kasai Algorithm
def build_lcp_array(s: str, n, suffix_array: Ptr[Int[32]]) -> List[int]:
    rank = List[int]([0] * n)

    for i in range(n):
        rank[int(suffix_array[i])] = i

    k = 0
    lcp = List[int]()

    print(f'Init lcp: {lcp}')

    # for i in range(n):
    #     lcp[i] = 0

    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = int(suffix_array[rank[i] + 1])
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1

    return lcp


def main():
    Text = "abracadabra"
    n = len(Text)
    SA = Ptr[Int[32]](n)
    divsufsort(Text.c_str(), SA, n)

    lcp_array = build_lcp_array(Text, n, SA)

    print('---- Suffix Array ----')
    for i in range(n):
        print(f'SA[{i}] = {SA[i]}')

    print('LCP array:')
    # print(lcp_array)

    # print('Rank')
    # rank = List[Int[32]]([Int[32](0)] * n)
    # print(rank)

    # test = Array[Int[32]](12)

    # print(test)

main()
