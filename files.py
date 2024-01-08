def get_empoyees():
  file = open("empoyees.csv")
  reader = csv.DirectReader(file)
  users = {}
  for row in reader:
    users[row['username']] = row
  return users

def get_customers():
  file = open("customers.csv")
    reader = csv.DictReader(file)
    customers = {}
    for row in reader:
        customers[row['name']] = row 
    file.close()
    return customers 
  
