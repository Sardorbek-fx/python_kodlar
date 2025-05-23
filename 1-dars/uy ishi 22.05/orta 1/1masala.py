yigindi = 0

for son in range(1, 501):
    if son % 2 != 0:
        yigindi += son

yigindi_str = str(yigindi)
if yigindi_str == yigindi_str[::-1]:
    print("Yigindi polindrom son")
else:
    print("Yigindi polindrom son emas")

print("Yigindi:", yigindi)
