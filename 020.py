from decimal import *
m, p, q = list(map(int, input().split()))
tmp_m = m - m * p / 100
after_m = Decimal(tmp_m) - Decimal(tmp_m) * q / 100
print(Decimal(after_m))
