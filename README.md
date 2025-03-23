# MILP Problem Solver

This project aimed to determine an optimal selection of areas/polygons from a given dataset based on adjacency and cost constraints.
I understand this solution is incomplete; however, I am willing to 

## Setup
This setup assumes that the current computer is on Windows.
1. Download and install Anaconda from [the official Anaconda website](https://www.anaconda.com/download/success).
2. Clone this repository in your choice of folder.
3. Open an Anaconda Prompt or Anaconda PowerShell Prompt in your cloned repo and run the following commands to install the necessary libraries. Agree to each prompt which prompted.
   
   ```conda install -c conda-forge pyomo shapely rasterio geopandas```
4. Download GPLK for Windows from [this link](https://winglpk.sourceforge.net/#download), and copy the glpk-#.### folder into C:\\.
5. You are now free to run the Jupyter Notebook (solution.ipynb).

## Credits / References
Much of my work would not have been possible were it not for the following resources and many others:
* [https://stackoverflow.com/questions/32316069/pyomo-cant-locate-glpk-solver](https://stackoverflow.com/questions/32316069/pyomo-cant-locate-glpk-solver)
* [https://www.datacamp.com/tutorial/pyomo](https://www.datacamp.com/tutorial/pyomo)
* [https://bobbyhadz.com/blog/conda-create-and-install-requirements-txt](https://bobbyhadz.com/blog/conda-create-and-install-requirements-txt)
