"""print("Hello")
raise Exception("This is an exception")  # this prompts a traceback error message
print("Bye")"""
# the above code is me creating an error to crash the program


###


print("Hello")
try:
    raise Exception("This is an exception")
except Exception:
    print("Exception is handled.")

print("Bye")

raise ZeroDivisionError("Because why not?")