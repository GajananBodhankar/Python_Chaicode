# Method Resolution Order (MRO)
# a solution to multipath inheritance like java, c++ each language has it's
# own approach to solve.

class A:
    label="I am label A"

class B:
    label="I am label B"

class C(A,B):
    def printLabel(self):
        print(" My label is ", self.label)
    
result= C()
print(C.__mro__)
result.printLabel() # prints my label is A if (A, B) and prints label B if (B, A)
# hence multiple inheritance problem solved
