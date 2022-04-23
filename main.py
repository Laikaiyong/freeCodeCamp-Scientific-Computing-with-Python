class Category:
  def __init__(self, category_name):
    self.name = category_name
    self.ledger = []

  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item['amount']

    return total
  
  def deposit(self, amount, description):
    self.ledger.append({
      'amount': amount,
      'description': description
    })

  def withdraw(self, amount, description="Withdrawal"):
    if self.check_funds(amount):
      self.ledger.append({
        'amount': -amount,
        'description': description
      })
      return True
    else:
      return False

  def transfer(self, amount, object):
    transferable = self.check_funds(amount)
    if transferable:
      self.withdraw(amount, "Transfer to " + object.name)
      object.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False

  def __str__(self):
    pattern = "*" * 12
    full_text = pattern + self.name + pattern + "*\n"
    for item in self.ledger:
      full_text += item['description'][0:23].ljust(24, " ") + "%.2f\n" % item['amount']

    full_text += "Total: " + str(self.get_balance())
    return full_text
    
def create_spend_chart(categories):
  full_text = "Percentage spent by category\n"

  each_total = [category.get_balance() for category in categories]
  total = sum(each_total)
  percentile = [ round(subtotal/total * 100, -1) for subtotal in each_total]
  for tenths in range(10):
    percentage = 100 - tenths * 10
    full_text += str(percentage).rjust(3, " ") + "|" 
    for percent in percentile:
        if percent >= percentage:
            full_text += " o "
        else:
            full_text += "   "
    full_text += '\n'

  full_text += " " * 4 + "-" * 9 + "\n"
  each_name = [category.name for category in categories]

  for index in range(len(max(each_name, key=len))):
    full_text += " " * 3
    for name in each_name:
      try:
        full_text += " " + name[index] + " "
      except:
        full_text += " " * 3
    full_text += "\n"
    
  return full_text

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))