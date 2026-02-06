
## How to run
In order to run the code use the following command in the base directory:
```
python part2-divide-and-conquer/src/naive.py data/a.txt data/b.txt data/c.txt 
```


### Note:
I am using slices of the matrices instead of indexing. While slicing lists in python might create copies, in numpy by default slice behavior is to create a view, thus no unecessary copies are created
