  
class Patient:
    def __init__(self, id, name, allergies, bed_number = None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
        
 
class Hospital:
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        
    def admit(self, patient):
        if type(patient) == Patient:
            if len(self.patients) < self.capacity:
                patient.bed_number = len(self.patients) + 1
                self.patients.append(patient)
            else:
                print(f"{self.name} has reach it's maximum patient capacity.")
                
    def discharge(self, id):
        for patient in self.patients:
            if patient.id == id:
                patient.bed_number = None
                self.patients.remove(patient)
                
                
st_judge = Hospital('Saint Jude', 2)
oshil = Patient(1, 'John', 'leds')
oshil_1 = Patient(2, 'Jack', 'rice')
oshil_2 = Patient(3, 'Mack', 'fly')

st_judge.admit(oshil)
st_judge.admit(oshil_1)
st_judge.admit(oshil_2)
print(oshil.bed_number)
print(oshil_1.bed_number)
print(oshil_2.bed_number)

for patient in st_judge.patients:
    print(patient.name)