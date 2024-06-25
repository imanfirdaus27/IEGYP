name = "David"
batch = 101 
fee = 1245.6578
# traditionaly how we do this
inputstring = "Hello" + name + ", welcome to python class " + str(batch)
print(inputstring)

# how much of space is required
inputstring = f"Hello{name:40s}, welcome to python class {batch}"
print(inputstring)

# align david to center
inputstring = f"Hello{name:^40s}, welcome to python class {batch}"
print(inputstring)

# align david to right
inputstring = f"Hello{name:>40s}, welcome to python class {batch}"
print(inputstring)

# padding character
inputstring = f"Hello{name:*>40s}, welcome to python class {batch}"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# Let us focus on decimal
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)


# Let us focus on decimal
inputstring = f"Hello {name:.3}, welcome to python class {batch:< 10d} in KL"
print(inputstring)

# Let us focus on decimal
inputstring = f"Hello {name:.3}, welcome to python class {batch:< 10d} in KL for RM{fee:10.2f}"
print(inputstring)

# Let us focus on decimal
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM{fee:10.2f}"
print(inputstring)

# octal value
inputstring = f"Hello {name:.3}, welcome to python class {batch:o} in KL for RM{fee:10.2f}"
print(inputstring)

# octal value
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:10.2f}"
print(inputstring)

# octal value
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:1,.2f}"
print(inputstring)