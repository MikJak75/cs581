
## How to run
In order to run the code use the following command in the base directory:
```
python part3-strassen/src/naive.py data/a.txt data/b.txt data/c.txt 
```


### Note:
I am using slices of the matrices instead of indexing. While slicing in python lists might create copeis, in numpy by default slice behavior is to create a view, thus no unecessary copies are created
