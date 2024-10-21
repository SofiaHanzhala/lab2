def expression(x):

  import math 
  z = (math.sqrt(2)/2)*math.sin(1/x)+1
  return z
while True:
  x = int(input("Введіть значення x: "))
  if x != 0:
    break
  else:
    print("Помилка: х не може бути 0. Введіть інше значення")
  
print ("Значення виразу z= ", expression(x))

def product(n):
  divisors_sum = sum([i for i in range(1, n) if n % i == 0])
  return divisors_sum < n
n = int(input("Введіть число n: ")) 
if product(n):
  print(f"Число {n} є недостатнім")
else:
  print(f"Число {n} не є недостатнім")
