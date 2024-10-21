from mod import product

n = int(input("Введіть число n: ")) 
if product(n):
  print(f"Число {n} є недостатнім")
else:
  print(f"Число {n} не є недостатнім")
