# ECE143-Individual-Project
This repository contains the code for the Individual Project by Humberto Hernandez (A11452300) for the course ECE 143 at the University of California, San Diego.

Please keep everything in the same directory.

If using the Spyder IDE, I recommend attempting to run the plotting functions so that it plots in a separate window. Usually what I'll do is I'll run the file, cancel it the run, write "%matplotlib auto" in the console and try again.

The code that runs pretty much everything is the tower_coverage.py file. Those include the functions for plotting up to n towers and the function that tells you the average amount of towers needed to cover the desired coverage area.

Note: If using something other than Spyder or the Jupyter Notebook. You may or may not have to add a "plt.show()" line to display the plot if you have the plotting enabled.

I've had issues before where sometimes the assert statements will trigger falsely in Spyder. I recommend re-running the files in the following order. tower_class.py file first and then running the tower_coverage.py file.

plotting_code_proj.py --> tower_class.py -- > tower_coverage.py --> test_tower_class.py
If it's still an issue, you can just comment out the assert statements and the code will still work.

For running the test_tower_class.py, I recommend running that as the main file if you want to run the tests.
