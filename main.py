def convert_pennies(amount):
    dollars = amount // 100
    amount %= 100
    quarters = amount // 25
    amount %= 25
    dimes = amount // 10
    amount %= 10
    nickels = amount // 5
    pennies = amount % 5

    return dollars, quarters, dimes, nickels, pennies

def main():
    try:
      pennies_input = int(input("Enter the amount in pennies: "))
      if pennies_input == "quit":
         return False
      if pennies_input < 0:
        print("Please enter a non-negative number of pennies.")
        return True
      else:
        dollars, quarters, dimes, nickels, pennies = convert_pennies(pennies_input)

        print(f"Dollars: {dollars}")
        print(f"Quarters: {quarters}")
        print(f"Dimes: {dimes}")
        print(f"Nickels: {nickels}")
        print(f"Pennies: {pennies}")
        return True
    except ValueError:
      print("Please enter a valid number of pennies.")
      return True

while main():
  pass
