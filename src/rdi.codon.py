from bio import *
import sys
import datetime

LIBDIVSUFSORT="lib/libdivsufsort.so.3"
from C import LIBDIVSUFSORT.divsufsort(ptr[byte], Ptr[Int[32]], int)

# Kasai Algorithm
def build_lcp_array(s: str, n, suffix_array: Ptr[Int[32]]) -> List[int]:
    lcp = List[int]([0] * (n))
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

    return [0] + [0] + lcp + [0]


def main():
    start = datetime.datetime.now()
    for ref_genome in FASTA('data/test.fa', fai=False, validate=False, gzip=False):
        
        Text = str(ref_genome.seq).upper()
        # Text = "ACTACG"
        n = len(Text)
        SA_ptr = Ptr[Int[32]](n)
        
        divsufsort(Text.c_str(), SA_ptr, n)

        SA = List[int]([n])

        for i in range(n):
            SA.append(int(SA_ptr[i]))

        LCP = build_lcp_array(Text, n, SA_ptr)

        # print('---- Table 1 ----\n')
        # print('i \tSA[i]\tLCP[i]\tT[SA[i]..n]')
        # print
        # for i in range(n + 1):
        #     sa_index = int(SA[i])
        #     print(f'{i}\t{sa_index}\t{LCP[i]}\t{Text[sa_index:n]}$')

        # print ('\n')

        # Create RD Index
        index = list()

        for i in range(1, n + 1):
            if (LCP[i] < LCP[i + 1]):
                for k in range(LCP[i] + 1, LCP[i + 1] + 1):            
                    # Calculate j > i is the minimum value such that LCP[j] < LCP[i + 1]
                    j = -1

                    for j_test in range(i + 1, n + 2):
                        if (LCP[j_test] < k):
                            j = j_test
                            break

                    if j <= i: # Violates condition #2
                        continue

                    p = SA[i]
                    c = j - i
                    T = Text[p:p+k]

                    index.append( (p, k, c, T) )

        # print('\nRecords:\n\n')
        
        # for i in range(2):
        #     print(index[i])
        # for record in index:
        #     print(record)
    
    return datetime.datetime.now() - start

runtime = main()

print(f'{runtime.microseconds}')
