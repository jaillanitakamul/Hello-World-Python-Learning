'''
| Operation            | Symbol   | Method                      |              |
| -------------------- | -------- | --------------------------- | ------------ |
| Union                | \`A      | B\`                         | `A.union(B)` |
| Intersection         | `A & B`  | `A.intersection(B)`         |              |
| Difference           | `A - B`  | `A.difference(B)`           |              |
| Symmetric Difference | `A ^ B`  | `A.symmetric_difference(B)` |              |
| Subset               | `A <= B` | `A.issubset(B)`             |              |
| Superset             | `A >= B` | `A.issuperset(B)`           |              |
| Disjoint             | —        | `A.isdisjoint(B)`           |              |

'''

import os 
os.system('cls')
#[] list, () tuple, {} set
aSet={1,2,3,4}
bSet={3,4,5,6}
'''
# Union → all elements from both sets
print(aSet.union(bSet))
print(aSet | bSet)

#Intersection → common elements
print(aSet & bSet)
print(aSet.intersection(bSet))

#Difference → elements in A but not in B
print(aSet-bSet)
print(aSet.difference(bSet))
#elements in B but not in A
#print(bSet-aSet)

#Symmetric Difference 
# → elements in A or B, but not both

print(aSet^bSet)
print(aSet.symmetric_difference(bSet))

#Subset and SuperSet
#return (true, false)
aNum = {1,2,3}
bNum = {1,2,3,4,5}

print(aNum.issubset(bNum))
print(bNum.issuperset(aNum))

print(aNum <= bNum)
print(bNum >= aNum)

#Disjoint  -  no elements in common
p={1,2}
q={3,4}

print(p.isdisjoint(q))'''

