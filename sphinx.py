# 20180308
r"""
Good tutorial: https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html

# NOTE:
    #. Always use if __name__ == "__main__" to wrap the code, to avoid import errors.

$ pip install sphinx
$ mkdir docs
$ cd docs

$ sphinx-quickstart
    choose yes for : separate the source and build directories
            autodoc extension
conf.py
uncomment: conf.py sys.path.insert
modify sys.path.insert
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]
# napoleon extension is for google style comment.

html_logo = '_static/logo.png'

$ sphinx-apidoc -f -o source/ ../mypackage/
$ sphinx-apidoc -f -d2 -o source/ ../mypackage/

$ make html

latex
=====
#. use sphinx.ext.mathjax
#. Keep in mind that when you put math markup in Python docstrings read by autodoc, you either have to double all backslashes, or use Python raw strings (r"raw"). Just like this one.

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

import modules within the same folder as the source script
==========================================================


Sphinx + Github Pages

    1. touch docs/.nojekyll
    2. echo ''' <meta http-equiv="refresh" content="0; url=./build/html/index.html" /> ''' > docs/index.html
    3. make html

"""
