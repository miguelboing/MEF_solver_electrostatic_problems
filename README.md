
<h1 align = 'center'>Finite Element Method Solver for Electrostatic Problems</h1>
<h4>
This project solves 2D and linear electrostatic problems using the variational method. The data is inserted using a CSV file:</h4>


<h1><img src="https://ik.imagekit.io/xkg5lotj6iy/MEF_solver/Eletrostatic_problem_ekyn9VHlr.jpg"></h1>

<h4>The correspondent CSV table for this example:</h4>

<h1 align='center'><img src="https://ik.imagekit.io/xkg5lotj6iy/MEF_solver/CSV_table_IBrR3FFrWE.jpg"></h1>

<h3>The nodes</h3>

<h4>
The first, second and third columns are used to find the X, Y coordinates and potential of each node 
(the nodes that have unknown potentials need to be left in blank).
</h4>

<br/>

<h3>The elements</h3>

<h4>
The forth column is used to tell which nodes are from each elements in this example the first element is delimited
by the nodes 1, 2 and 4. The fifth column is used to describe what is the permissiveness of the 
specific element.</h4>

<h3>
The project uses:
</h3>

<h4>

- **Numpy library** to solve the linear equations;
- **CSV library** to work with the CSV data.

</h4>
<h4>When the function is executed it returns a list containing all the potentials from the nodes</h4>