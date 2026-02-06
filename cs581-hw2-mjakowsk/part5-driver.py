from part1_naive.src.naive import naive, load_matrix, store_matrix
from part2_divide_and_conquer.src.dandc import dandc
from part3_strassen.src.strassen import strassen

import numpy as np
import os

SIZES = [4, 8, 32, 128, 512]

def create_sets(sizes):
    dir_name = "part5-analysis/matrices/"
    for i in range(len(sizes)):

        set_name = dir_name + f"set_{i}/"
        # If the set doesn't exist already
        if os.path.exists(set_name) == False:
            os.mkdir(set_name)

            size = sizes[i]
            A = np.random.randint(0, 10000, (size, size))
            B = np.random.randint(0, 10000, (size, size))

            store_matrix(set_name + "A.txt", A)
            store_matrix(set_name + "B.txt", B)



if __name__ == "__main__":
    # generate the matricies

    create_sets(SIZES)


