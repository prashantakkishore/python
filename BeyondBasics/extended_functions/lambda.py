
# With function
def first_name(name):
    '''Get first name'''
    name.split()[0]

# With lambda
'''
1 - argument is name followed by colon
2 - multiple arguments separated by comma
3 - no argument lambda is followed by just colon eg lambda:
4 - cant have docstrings
'''
first_name_1 = lambda name: name.split()[0]



# EG
last_name = lambda name: name.split()[-1]
print(last_name('prashantak srivastava')) # srivastava