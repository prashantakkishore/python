def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list

def sequence_class_exp(immutable):
    tuple if immutable else list


'''
Conditional statement:

    if immutable:
        cls = tuple
    else:
        cls = list
        
-----------------------

Conditional expression

cls  = tuple if immutable else list
'''