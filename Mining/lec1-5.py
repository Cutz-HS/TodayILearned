# 간단 구구단
# 문제: 50 이상일 때, quit

sw = False
for i in range(2,10):
    if sw:
        break
    print(i, "단")
    for k in range(1, 10):
        if i*k >= 50:
            sw = True
            break
        print(i, " X ", k, "=", i*k)
    print("\n")