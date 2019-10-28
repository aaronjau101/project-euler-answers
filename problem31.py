def countChange(money, coins):
  if (money == 0):
      return 1
  elif (len(coins) == 0 or money < 0):
      return 0
  else:
      return countChange(money - coins[0], coins) + countChange(money, coins[1:])

a = [200, 100, 50, 20, 10, 5, 2, 1]
print(countChange(200, a))
