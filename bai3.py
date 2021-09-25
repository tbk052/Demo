def tinhgiaithua(num):
    giai_thua = 1
    if (num == 1):
        return giai_thua
    if (num > 1):
        for i in range(2, num + 1):
            giai_thua = giai_thua * i
        return giai_thua
    else:
        print("Vui lòng nhập số lại nguyên dương")
        return notAnum


notAnum = False
num = int(input("Nhập số nguyên dương: "))
print("Giai thừa của", num, "là", tinhgiaithua(num))
