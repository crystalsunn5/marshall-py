# Lesson 5

# Ask the user for the amount of money they have and the number of cookies purchased
money = input("Enter your initial amount of money:")
money = float(money)
cookies = input ("How many cookies were purchased? Enter c for normal cookies and b for big cookies:")
cookies = str(cookies)

# Calculate the total number of cookies
normalCookies = (cookies.count("c"))
bigCookies = (cookies.count("b"))
totalCookies = normalCookies + bigCookies
print(f"Client bought {totalCookies} cookies")

# Calculate profit
ncProfit = normalCookies * 1.25 - normalCookies * 0.5
bcProfit = bigCookies * 2 - bigCookies * 0.75
totalProfit = ncProfit + bcProfit
print(f"You made $ {totalProfit} in profit")

# Calculate amount of money left over
moneyAfter = money + totalProfit
print(f"You have $ {moneyAfter} now")

