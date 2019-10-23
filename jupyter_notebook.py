# Jupyter Python Notebook

!ls
# execute shell commands

#Just write latex in Markdown Cell. Then it's all good.
################################################################################
# magic methods

%matplotlib notebook
%matplotlib inline
%lsmagic

%env OMP_NUM_THREADS=4
# set environment variables

%run
# run: execute python code from .py files or notebook files

%load
# This will replace the contents of the cell with an external script. You can either use a file on your computer as a source, or alternatively a URL.

%%time
# single run of the code in your cell

%%timeit
# uses the Python timeit module which runs a statement 100,000 times (by default) and then provides the mean of the fastest three times.

%%writefile my_file.py
# saves the contents of that cell to an external file.
%pycat my_file.py
# Show the contents of an external file

%prun
# Show how much time your program spent in each function.

%config InlineBackend.figure_format = 'retina'
#  double resolution plot output

%%bash
# run the cell using bash kernel

my_statement;
# ';' suppress output

################################################################################
# to hide cell number, add the following in a cell
%%HTML
<style>
div.prompt {display:none}

table.dataframe {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
################################################################################
import os
from IPython.display import display, Image
display(Image(filename='image.png'))
display(Image(filename='image.png', embed=True)

################################################################################
# Cell operation:
# Tags
$ jupyter nbconvert --ExecutePreprocessor.timeout=600 --execute --to html Notebook/report.ipynb --output report.html --TagRemovePreprocessor.remove_input_tags={\"hide_input\"} --TagRemovePreprocessor.remove_all_outputs_tags={\"hide_output\"}
    
    # import subprocess
    # subprocess.call(["jupyter",
    #                  "nbconvert",
    #                  "--ExecutePreprocessor.timeout=600",
    #                  "--execute",
    #                  "--to",
    #                  "html",
    #                  ROOT_PATH + "Notebook/report.ipynb",
    #                  "--output",
    #                  CWD_PATH + "report.html",
    #                  "--TagRemovePreprocessor.remove_input_tags={\"hide_cell\"}"
    #                 ])
 
################################################################################
# Programatically Markdown
"Number: %f, Name: %4"%(1.11, 'text')


# Pandas styling

df.style.set_properties(**{'text-align': 'left', 'background': 'red'})
def highlight_cols(s):
    color = 'grey'
    return 'background-color: %s' % colorzR

df.style.applymap(highlight_cols, subset=pd.IndexSlice[:, ['B', 'C']])

