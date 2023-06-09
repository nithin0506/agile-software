def sum_n(n):

  s=0
  for i in range(0, n+1):
    s += i
    return s

print(f"{sum_n(10)}")
