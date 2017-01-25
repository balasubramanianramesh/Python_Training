list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [ 0, 1, 2, 3, 4, 5, 6, 7 ];

print "list2[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

print "list2[3:]: ", list2[3:] # list1[3::]
print "list2[::2]: ", list2[::2]
print "list2[::-2]: ", list2[::-2]
print "list2[::1]: ", list2[::1]
print "list2[2]: ", list2[2]
print "list2[-2]: ", list2[-2]

print "before Delete : "
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1

print "lenth of list2 : ", len(list2)

list3 = list1+list2
print list3

print 'compare list2 with list3 :', cmp( list2, list3 )
print 'compare list3 with list2 :', cmp( list3, list2 )

print 'max of list3 :', max(list3)
print 'min of list3 :', min(list3)

## operations

print 'list3 : ',list3
list3.append(2000) #Add at the end
print 'After Append : ', list3
print 'count of an object in list3 : ', list3.count(2000)
list3.extend( [ '2015', 2016, 'bala' ] ) #Add sequence at the end
print 'After extend : ', list3
print 'index of 2000 in list3 : ', list3.index(2000) #return the lowest index
#list3.index(8) # Error : ValueError: 8 is not in list
list3.insert(-1,'Janane') #insert 1 index before from last
print 'After insert : ', list3
#pop Removes and returns last object or obj from list
print 'After pop : ', list3.pop(2) #pop(<index>)
list3.remove('2015')
print 'After Remove "2015" from list3 : ', list3
list3.reverse()
print 'After Reverse : ', list3
list3.sort()
print 'After sort : ', list3