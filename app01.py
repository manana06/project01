import csv
"""
 connection of employees
"""
def login():
  username = input("Username: ")
  password = input("Passwprd: ")
  users =get_users()
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
def employees_role():
  name = input("Give a name: ")
  address = input( "Give an address: ")
  items = input( "Give the order: ")
  date = input("Give the date: "  )
  total = input("Give a total cost: ")

def get_empoyees():
  file = open("empoyees.csv")
  reader = csv.DirectReader(file)
  users = {}
  for row in reader:
    users[row['username']] = row
  file.close()
  return users

def get_customers():
  file = open("customers.csv")
    reader = csv.DictReader(file)
    customers = {}
    for row in reader:
        customers[row['name']] = row 
    file.close()
    return customers 

username, role = login()
while True:
  if role == 'clerk':
    choice = employees_role()
  elif role == 'manager':
 add
  elif role == 'delivery':
add
  else:
 add
  
