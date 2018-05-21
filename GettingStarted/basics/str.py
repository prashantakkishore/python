# Strings are immutable

colors = ';'.join(['12','23','43','2'])
print(colors)  # 12;23;43;2
print(colors.split(';')) # ['12', '23', '43', '2']

data = ' '.join(('Prashantak' , '34' ))
print(data)