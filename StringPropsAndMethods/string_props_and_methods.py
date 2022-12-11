# Immutable
first_name = 'Jake'
print(first_name[2])
# first_name[2] = "P"
# print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)

last_letter = first_name[-1:]
print(last_letter)

# Concatenable
new_first_name = first_two_letters + 'P' + last_letter
print(new_first_name)

greeting = "Hello"
greeting = greeting + " Python!"
print(greeting)

# Multiplication
yummy = "Yum "
print(yummy * 2)

result_upper = yummy.upper() * 3
result_lower = yummy.lower() * 3
print(result_upper)
print(result_lower)

long_str = "This is a loooong string"
print(long_str.split())
