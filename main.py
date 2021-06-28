from data_structures.linkedlist import LinkedList

l = LinkedList()

l.push(10)
l.push(40)
l.push(50)
l.push(30)
l.push(20)

print(l.to_str())
print(l.merge_sort().to_str())
