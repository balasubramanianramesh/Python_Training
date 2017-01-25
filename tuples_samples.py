tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = ( 0, 1, 2, 3, 4, 5, 6, 7 );
tup3 = "a", "b", "c", "d";
tup1 = (); ##Empty tuple
tup1 = (50,); ## To write a tuple containing a single value you have to include a comma, even though there is only one value
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
print "tup2[3:]: ", tup2[3:] # tup2[3::]
print "tup2[::2]: ", tup2[::2]
print "tup2[::-2]: ", tup2[::-2]
print "tup2[::1]: ", tup2[::1]
print "tup2[2]: ", tup2[2]
print "tup2[-2]: ", tup2[-2]

tup4 = tup1 + tup2 + tup3;
print tup4
print len(tup4)
print 10 in tup4
print 'a' in tup4
print "tup2 : ",tup2
print "tup4 : ",tup4
print tup2 in tup4 ## cann't able to check the tuples values
print 'compare tup2 with tup4', cmp( tup2, tup4 )
print 'compare tup4 with tup2', cmp( tup4, tup2 )
#del tup4   ## del tup4[2] ## will not work
#print tup4