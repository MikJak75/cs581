import argparse
import numpy as np

# assumes A and B are square matrices of size n x n, where n is a power of 2
def strassen(A, B):
    n = A.shape[0]

    C = np.zeros((n, n), dtype=int)

    if n == 1:
        C[0, 0] = A[0, 0] * B[0, 0]
    else :
        # By default numpy makes these views, so no data is copied
        A11 = A[0:n//2, 0:n//2]
        A12 = A[0:n//2, n//2:n]
        A21 = A[n//2:n, 0:n//2]
        A22 = A[n//2:n, n//2:n]

        B11 = B[0:n//2, 0:n//2]
        B12 = B[0:n//2, n//2:n]
        B21 = B[n//2:n, 0:n//2]
        B22 = B[n//2:n, n//2:n]

        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12

        P1 = strassen(A11, S1)
        P2 = strassen(S2, B22)
        P3 = strassen(S3, B11)
        P4 = strassen(A22, S4)
        P5 = strassen(S5, S6)
        P6 = strassen(S7, S8)
        P7 = strassen(S9, S10)

        C11 = P4 + P5 + P6 - P2
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P5 + P1 - P3 - P7

        C = np.block([[C11, C12], [C21, C22]])

    return C

def load_matrix(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
        m = int(lines[0].strip().split()[0])
        n = int(lines[0].strip().split()[1])

    C = np.zeros((int(m), int(n)), dtype=int)

    for i, line in enumerate(lines[1:]):
        val_list = line.strip().split()
        for j in range(n):
            C[i, j] = int(val_list[j])
    
    #print(f"{m} x {n}")
    return C


def store_matrix(fname, C):
    m = C.shape[0]
    n = C.shape[1]

    with open(fname, 'w') as f:
        f.write(f"{m} {n}\n")
        for i in range(m):
            row = " ".join([str(C[i, j]) for j in range(n)])
            f.write(f"{row}\n")

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments)")
    parser.add_argument("f1", type=str)
    parser.add_argument("f2", type=str)
    parser.add_argument("f3", type=str)

    args = parser.parse_args()

    f1 = args.f1
    f2 = args.f2
    f3 = args.f3

    A = load_matrix(f1)
    B = load_matrix(f2)

    C = strassen(A, B)

    #print (A@B)

    store_matrix(f3, C)

    exit()