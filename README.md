## matrix-graphing-and-transformation

A python program to multiply, graph, and transform matricies. It can take input from the user or input from files in the same directory. The format for the matricies is the following: the transformation matrix is a 2 by 2 matrix and the matrix to be multiplied by is a 2 by n matrix where each *column* is represents a 2-d coordinate in the form (x,y). The program wont run successfully if the dimensions are different. The program only graphs the initial matrix and the final transformed matrix (although you can graph other 2 by n matricies if you'd like with the `graph_matrix` function). 

# How to Run
Open terminal and navigate to the desired folder of storage.

Clone the repository into desired folder with `git clone https://github.com/AndrewTShen/matrix-graphing-and-transformation`.

Change the `matrix.txt` and `transformationMatrix.txt` contents to the desired matricies. If you'd like, you can also change 
the program itself to accept input from user input using the `matrix_io_input`.

In the `matrix-graphing-and-transformation` folder, run `ipython matrix_graph_transform.py`.

A screen should pop up with the original matrix and the new, transformed matrix graphed.
