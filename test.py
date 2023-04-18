def is_prime_number(number):
  for i in range(2, number):
    if number % i == 0:
      return False
  return True


print(f"{is_prime_number(73)}")
