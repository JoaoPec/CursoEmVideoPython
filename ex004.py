#Mostrar tipo primimtivo e  todas as informações possíveis sobre ela 

n = input('')
print('Data type is: ',type(n))
print('It is printable? ',n.isprintable())
print('It is a num?',n.isalnum())
print('It is alphanumeric?',n.isalpha())
print('Are ascii?',n.isascii())
print('Are decimal?',n.isdecimal())
print('It is a digit?',n.isdigit())
print('It is an identifier?',n.isidentifier())
print('') # empty line
print('It contains only letters and numbers?', n.isalnum())
print('It is a titlecased string?', n.istitle())
print('It is a lowercase string?', n.islower())
print('It is a uppercase string?', n.isupper())
print('It is a whitespace string?', n.isspace())
print('It is a string starting with a capital letter?', n.istitle()) 
