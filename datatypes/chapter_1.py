num=2
print("Initial amount is", num)

num=10
print("Mutated amount is", num)

print("Id of 2 is", id(2))
print("Id of 12 is", id(10))

# ============================================================================

numSet=set()
print("set before ", numSet, "address: ", id(numSet))
for i in range(1, 10):
    numSet.add(i)
print("set after ", numSet, "address: ", id(numSet))

