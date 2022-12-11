greeting = "Hello"
first_name = "Jack"
last_name = "White"
exclamation_sign = "!"
white_space = " "
whole_sentence = greeting + white_space + first_name + \
                 white_space + last_name + exclamation_sign
long_string = "This is the long string"
print(whole_sentence)

# Escaping
some_string = 'I\'m a programmer'
print(some_string)
another_string = "I want to learn \"Python\""
print("TEST >>", another_string)

string_with_new_lines = f"Hello!\n My name is {first_name}"
print(string_with_new_lines)

numbers = "1\t234567"
print(numbers)

some_text = "\t Hello! \n I`m very glad to see you!"
print(some_text)

# Triple quotes
string_with_triple_quotes = """This is text
                                with "triple quotes" """
print(string_with_triple_quotes)
another_string_with_triple_quotes = '''This is another text with "triple quotes" '''
print(another_string_with_triple_quotes)
