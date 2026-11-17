class Patient: #Creates the Parent class
    def __init__(self, name, bill_amount): #Initiates the objects
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self): #returns the object "name"
        return self.name

    def get_bill_amount(self): #returns the object "bill_amount"
        return self.bill_amount

    def set_name(self, name): #overrides the original value of the object "name"
        self.name = name

    def set_bill_amount(self, bill_amount): #overrides the orignal value of the object "bill_amount"
        self.bill_amount = bill_amount

    def calculate_bill(self): #calculates for the final bill accounting for discounts
        return self.bill_amount

    def display_patient_type(self): #displays if the patient is a "Regular Patient", "Senior Citizen", or "PhilHealth Member"
        print("Regular Patient")

class Senior_Patient(Patient): #Creates the sub-class "Senior_Patient" from the Parent class "Patient"
    def calculate_bill(self): #overrides the function "calculate_bill" to now calculate for a 20% discount
        return (80 * self.bill_amount) / 100
 
    def display_patient_type(self): #Displays the patient type "Senior Citizen"
        print("Senior Citizen")

class PhilHealth_Patient(Patient): #Creates the sub-class "PhilHealth_Patient" from the Parent class "Patient"
    def calculate_bill(self): #overrides the function "calculate_bill" to now calculate for a 15% discount
        return (85 * self.bill_amount) / 100

    def display_patient_type(self): #Displays the patient type "PhilHealth Member"
        print("PhilHealth Member")

print("Hospital Billing System")
print("-----------------------")
p1 = Patient("Juan Dela Cruz", 15000) #Initializes the object's value
print(f"Patient: {p1.get_name()}") #prints the Patient's name
p1.display_patient_type() #Displays the Patient's type
print(f"Original Bill: P{p1.get_bill_amount():,.2f}") #Displays the Original bill
print(f"Final Bill: P{p1.calculate_bill():,.2f}\n") #Displays the final calculated bill

s1 = Senior_Patient("Maria Santos", 15000)
print(f"Patient: {s1.get_name()}") 
s1.display_patient_type()
print(f"Original Bill: P{s1.get_bill_amount():,.2f}")
print(f"Final Bill: P{s1.calculate_bill():,.2f}\n") #Displays the final calculated bill, with the discount of 20%

pm1 = PhilHealth_Patient("Pedro Reyes", 15000)
print(f"Patient: {pm1.get_name()}") 
pm1.display_patient_type()
print(f"Original Bill: P{pm1.get_bill_amount():,.2f}")
print(f"Final Bill: P{pm1.calculate_bill():,.2f}") #Displays the final calculated bill, with the discount of 15%
