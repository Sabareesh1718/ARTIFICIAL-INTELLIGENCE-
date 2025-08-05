m=[[12, 24, 36],[45, 54, 63]]

t=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

for row in t:
    print(row)
