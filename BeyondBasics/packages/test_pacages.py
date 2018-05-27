'''
Packages are directories with __init__.py file inside it

'''

import urllib
import urllib.request

'''
Packages are directories and Modules are single files
'''
print(type(urllib)) # <class 'module'> [Its a Package]
print(type(urllib.request)) # <class 'module'> [Its a Normal module]

print(urllib.__path__)  #   ['/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib']  ------ So its a dir so a Package
# print(urllib.request.__path__) # Exception AttributeError: module 'urllib.request' has no attribute '__path__ [So its not a package its a module]

import reader_dir
print(type(reader_dir)) # <class 'module'>
# print(reader_dir.__file__) # AttributeError: module 'reader_dir' has no attribute '__file__'

'''
__int__.py file is executed when package modules are imported
'''
import reader_pkg
print(type(reader_pkg)) # <class 'module'>
print(reader_pkg.__file__) # /Users/prashsr2/projects/mygit/python/BeyondBasics/packages/reader_pkg/__init__.py

'''
To get reader module without importing from __init__.py
'''
import reader_pkg.reader
print(reader_pkg.reader.Reader().my_reader())

'''
To get reader module with importing from __init__.py
'''
import reader_pkg
print(reader_pkg.Reader().my_reader())




