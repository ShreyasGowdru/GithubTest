L = [1, 2, 3, [1, 2, 'naveen'], 4, 5]


#alist = [1, 2, 3, 1, 2, 'naveen', 4, 5]

'''pos1 = 0
pos2 = 0

for i in range(pos1):   
    for j in range(pos2):
        if alist[pos2] == 'naveen':
            print('The position is :' + str(pos2))
            break
        else:
            pos2 += 1
            continue
pos1 += 1'''


'''for i in range(pos):
    while True:
        if alist[pos] == 'naveen':
            print('The position is :' + str(pos)+ ' index position')
            break
        else:
            print('naveen not found in :' + str(pos) + ' index position')
            pos += 1'''

#pos = (0)

'''for i in range(0, 6):
    for j in range(0, 3):
        if alist[3][2] == 'naveen':
            print('The position is : ' + str() + 'index position')
            break
        else:
            print('naveen not found')
            #pos += 1



#print(alist[3][2])'''

'''if __name__ == '__main__':
    for _ in range(int(input())):
        name = 5
        score = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

        score = score.sort(key = str.lower())
        print(score)

list.pop()'''


'''L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print('L[0]: ' + L[0])
print('L[1]: ' + L[1])
print('L[2]: ' + str(L[2]))
print('L[2][0]: ' + L[2][0])
print('L[2][1]: ' + L[2][1])
print('L[2][2]: ' + str(L[2][2]))
print('L[2][2][0]: ' + L[2][2][0])
print('L[2][2][1]: ' + L[2][2][1])
print('L[3]: ' + str(L[3]))
print('L[4]: ' + L[4])'''

#Change Nested List Item Value
#You can change the value of a specific item in a nested list by referring to its index number.
'''L = ['a', ['bb', 'cc'], 'd']
L[1][1] = 0
print(L)    #['a', ['bb', 0], 'd']'''

#Add items to a Nested list
#To add new values to the end of the nested list, use append() method.
'''L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L) #['a', ['bb', 'cc', 'xx'], 'd']'''

#When you want to insert an item at a specific position in a nested list, use insert() method.
'''L = ['a', ['bb', 'cc'], 'd']
L[1].insert(0, 'aa')
print(L)    #['a', ['aa', 'bb', 'cc'], 'd']'''

#You can merge one list into another by using extend() method.
'''L = ['a', ['bb', 'cc'], 'd']
L[1].extend([1, 2, 3])
print(L)       #['a', ['bb', 'cc', 1, 2, 3], 'd']'''

#Remove items from a Nested List
#If you know the index of the item you want, you can use pop() method. It modifies the list and returns the removed item.
'''L = ['a', ['bb', 'cc', 'dd'], 'd']
L[1].pop(1)
print(L)    #['a', ['bb', 'dd'], 'd']'''

#If you don’t need the removed value, use the del statement.
'''L = ['a', ['bb', 'cc', 'dd'], 'd']
#L[1].__delitem__(1)
#or del L[1][1]
print(L)    #['a', ['bb', 'dd'], 'd']'''

#If you’re not sure where the item is in the list, use remove() method to delete it by value.
'''L = ['a', ['bb', 'cc', 'dd'], 'd']
L[1].remove('cc')
print(L)    #['a', ['bb', 'dd'], 'd']'''

#Find Nested List Length
#You can use the built-in len() function to find how many items a nested sublist has.
'''L = ['a', ['bb', 'cc'], 'd']
print(len(L))   # 3 '''

#Iterate through a Nested List
'''L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in L:
    for j in i:
        print(j, end=' ')'''




