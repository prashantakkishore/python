# import path_test # ModuleNotFoundError: No module named 'path_test'
import sys
sys.path.append('not_searched')
import path_test
path_test.found()

# Can use env variable PYTHONPATH
# PYTHONPATH dirs auto appended in sys.path

