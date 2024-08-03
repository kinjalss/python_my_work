print("Hello World", 7)
print(5)
print("Bye")
print(17*13)

# A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.
# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
# The syntax of a print statement looks something like this:
# print(object(s), sep=separator, end=end, file=file, flush=flush)
# Other Parameters of Print Statement
# object(s): Any object, and as many as you like. Will be converted to string before printed
# sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# end='end': Specify what to print at the end. Default is '\n' (line feed)
# file: An object with a write method. Default is sys.stdout