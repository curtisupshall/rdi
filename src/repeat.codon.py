from bio import *

LIBDIVSUFSORT="lib/libdivsufsort.so.3"
from C import LIBDIVSUFSORT.divsufsort(ptr[byte], Ptr[Int[32]], int)

# Kasai Algorithm
def build_lcp_array(s: str, n, suffix_array: Ptr[Int[32]]) -> List[int]:
    lcp = List[int]([0] * (n + 1))
    rank = List[int]([0] * n)
    k = 0

    for i in range(n):
        rank[int(suffix_array[i])] = i

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
    LCP = build_lcp_array(Text, n, SA)

    print('---- Suffix Array ----')
    for i in range(n):
        sa_index = int(SA[i])
        print(f'SA[{i}] = {sa_index}: {Text[sa_index:n]}')


    # Create RD Index

    index = list()

    for i in range(n):
        if (LCP[i] >= LCP[i + 1]): # TODO may need to add LCP(N + 1) = 0
            continue # Violates condition #1


        sa_index = int(SA[i])
        for k in range(sa_index, n):            
            # Calculate j > i is the minimum value such that LCP[j] < LCP[i + 1]
            j = -1

            for j_test in range(i + 1, n + 1):
                if (LCP[j_test] < LCP[i + 1]):
                    j = j_test
                    break

            if j <= i: # Violates condition #2
                break

            if (LCP[i] >= k or k > LCP[i + 1]):
                continue # Violates condition #3

            r = i - j
            l = n - k
            index.append({ l:l, r:r, i:i, j:j, k:k })




    print('LCP array:')
    print(LCP)
    
    print(index)

main()
