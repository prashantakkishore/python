print('reader_pkg __init__ called')

from packages.reader_pkg.reader import Reader

# relative imports
#from .reader import Reader

# __all__ limit packages imported by 'import *'
from packages.reader_pkg.reader import Printer as TestPrinter
__all__ = ['TestPrinter']