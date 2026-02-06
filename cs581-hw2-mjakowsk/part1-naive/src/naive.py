import argparse
import numpy as np

def naive(A, B):
    ma = A.shape[0]
    na = A.shape[1]

    mb = B.shape[0]
    nb = B.shape[1]

    if na != mb:
        raise ValueError("Incompatible matrix dimensions")

    C = np.zeros((ma, nb), dtype=int)


    for i in range(ma):
        for j in range(nb):
            for k in range(na):
                C[i, j] += int(A[i, k] * B[k, j])
                
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


    A = load_matrix(f1)
    B = load_matrix(f2)

    C = naive(A, B)

    store_matrix(f3, C)

    #load_matrix(f1)


    exit()