from t2_permutations.perm import *
# Create a test permutation of length 20
q = testPermutation(20)
print(q)
# Define a permutation of length 10
p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
print(p)
printPermutation(p)
print(isTrivial(p))
print(p[0])
print(cycles(p))
# Create a trivial permutation of length 10
r = trivialPermutation(10)
print(r)
printPermutation(r)
print(r[0])
print(isTrivial(r))