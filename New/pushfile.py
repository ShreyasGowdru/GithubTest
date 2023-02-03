l = [-5, -23, 5, 0, 23, -6, 23, 67]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[j], l[i] = l[i], l[j]
print(l)
