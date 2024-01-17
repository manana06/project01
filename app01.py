import csv

#connection of employees

def login():
  username = input("Username: ")
  password = input("Passwprd: ")
  users =get_employees()
  if username in users:
    if password == users[username]['password'] and users[username]['active'] == '1':
      role = users[username]['role']
    else:
      role = None
  else:
    role = None
  return username , role


#imformations of customers

def add_customers():
    """
    Gets customrs data from the user, generated the next id,
    based on the size of the customers file, and then appends
    the new order to the customers.csv
    """
    name = input("Give name: ")
    address = input( "Give an address: ")
    items = input( "Give the order: ")
    date = input("Give the date (yyyy-mm-dd): "  )
    total = input("Give a total cost: ")
    orders = get_orders()
    new_id = len(customers) + 1
    file = open('customers.csv', 'a')
    file.write(str(new_id)+','+name+','+items+','
               +total+','+date+'\n')
    file.close()

def export_orders():
    cid = input("Give customer ID: ")
    customer = get_customer_by_id(cid)
    if customer is None:
        print("Customer not found.")
    else:
        file = open("customer" + cid + ".txt", "w")
        file.write("CUSTOMER REPORT\n")
        # write the basic CUSTOMER's data
        file.write("Name: " + customer['name'] + '\n')
        file.write("Address: " + customer['address'] + '\n')
        file.write("Items: " + customer['items'] + '\n')
        file.write("Date: " + customer['date'] + '\n')
        file.write("=================================\n")
        file.write("TREATMENTS\n")
        orders = get_orders()
        for key in orders:
            if orders[key]['customer_id'] == cid and orders[key]['delivered'] == '1':
                file.write(orders[key]['date'] + ", " +
                           orers[key]['items'] + '\n')

def get_customer_by_id(cid):
    """
    Finds the customer of the given id and return it. 
    If is not in the file, return None.
    """
    file = open(customers.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] == cid:
            return row 
    file.close()
    return None


def print_delivered_orders():
    orders = get_orders()
    for key in orders:
        if orders[key]['delivered'] == '1':
            print(key, orders[key]['date'],
                  oredrs[key]['time'], 
                  orders[key]['order'])

def get_orders():
    file = open("customers.csv")
    reader = csv.DictReader(file)
    orders = {}
    for row in reader:
        orders[row['id']] = row
    file.close()
    return orders

            
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

def get_orders():
    """
    Reads orders from the customers.csv file and returns a 
    dictionary with id as the key and a the respective customers's
    record as a value.
    """
    file = open("customers.csv")
    reader = csv.DictReader(file)
    customers = {}
    for row in reader:
        customers[row['id']] = row 
    file.close()
    return customers 


username, role = login()
while True:
  if role == 'clerk':
    add_customers()
    if delivered == 'Y':
     print("Order is delivered")
    elif delivered == 'N':
     print("Τhe order is pending..")
    else:
     print("Something is wrong!")
  elif role == 'manager':
     export_orders()
  elif role == 'delivery':
     print_open_orders()
  else:
     pass
  
