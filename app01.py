import csv
"""
 connection of employees
"""
def login():
  username = input("Username: ")
  password = input("Passwprd: ")
  users =grt_users()
  if username in users:
    if password == users[username]['password'] and users[username]['active'] == '1':
      role = users[username]['role']
    else:
      role = None
  else:
    role = None
  return username , role

"""
 connection of customers
"""
def all_clerks():
  name = input("Give a name: ")
  address = input( "Give an address: ")
  items = input( "Give the order: ")
  date = input("Give the date: "  )
  total = input("Give a total cost: ")
