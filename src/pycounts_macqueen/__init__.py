# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_macqueen")

# populate package namespace
from pycounts_macqueen.pycounts import count_words
from pycounts_macqueen.plotting import plot_words
