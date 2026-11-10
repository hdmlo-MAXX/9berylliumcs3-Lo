class Patient:
 def __init__(self, name, bill_amount):
   self.name = name
   self.bill_amount = bill_amount

  def get_name():
    return self.name

  def get_bill_amount():
    return self.bill_amount

  def set_name(name):
    self.name = name

  def set_bill_amount(bill_amount):
    self.bill_amount = bill_amount

  def calculate_bill(bill_amount):
    return (100 * bill_amount) / 100

  def display_patient_type():
    print("Regular Patient")

class Senior_Patient(Patient):
  def calculate_bill(bill_amount):
    return (80 * bill_amount) / 100

  def display_patient_type():
    print("Senior Citizen")

class Senior_Patient(Patient):
  def calculate_bill(bill_amount):
    return (80 * bill_amount) / 100

  def display_patient_type():
    print("PhilHealth Member")
