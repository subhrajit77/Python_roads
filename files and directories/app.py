from pathlib import Path
#absolute path
#relative path

path = Path("ecommerce")
print(path.exists())

path = Path("pacakges/ecommerce")
print(path.exists())

# make a path

# path = Path("emails")


# path = Path("packages/emails")
# print(path.mkdir())

#remove a dir

# path = Path("packages/emails")
# print(path.rmdir())

# finding files in a directory
path = Path("Modules")
# print(path.glob("*.py"))
# instead we include for loop to iterate over every single files

for file in path.glob('*.py'):
    print(file)
