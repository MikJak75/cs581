import argparse
import numpy as np

# assumes A and B are square matrices of size n x n, where n is a power of 2
def dandc(A, B):
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

        C11 = dandc(A11, B11) + dandc(A12, B21)
        C12 = dandc(A11, B12) + dandc(A12, B22)
        C21 = dandc(A21, B11) + dandc(A22, B21)
        C22 = dandc(A21, B12) + dandc(A22, B22)

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

    #print(f"Name: {args.f1}, Age: {args.f2}")
    f1 = args.f1
    f2 = args.f2
    f3 = args.f3


    #A = load_matrix(f1)
    #B = load_matrix(f2)

                   
    A = np.array([
        [1, 0, 0, 0,],
        [0, 1, 0, 0,],
        [0, 0, 1, 0,],
        [0, 0, 0, 1,],
    ])

    B = np.array([
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
    ])

    D = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16],
    ])

    A = D

    C = (A @ B)
    
    C = dandc(A, B)

    print(C)
    print(A@B)

    #C = dandc(A, B)

    #store_matrix(f3, C)

    exit()