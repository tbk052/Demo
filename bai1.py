A = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
B = []
for x in A:
    if x < 30:
        B.append(x)
print(B)

num = input("Nhap so bat ky: ")

for y in B:
    if (y > num):
        print(y)
