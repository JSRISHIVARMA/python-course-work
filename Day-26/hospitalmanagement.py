from abc import ABC, abstractmethod

# ------------------ Abstraction ------------------
class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# ------------------ Encapsulation ------------------
class Patient(Person):

    def __init__(self, name, age, disease):
        self.__name = name
        self.__age = age
        self.__disease = disease

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_disease(self):
        return self.__disease

    # Setter method
    def set_disease(self, disease):
        self.__disease = disease

    def display(self):
        print("\nPatient Details")
        print("Name :", self.__name)
        print("Age :", self.__age)
        print("Disease :", self.__disease)


# ------------------ Inheritance ------------------
class Doctor(Person):

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def display(self):
        print("\nDoctor Details")
        print("Name :", self.name)
        print("Specialization :", self.specialization)


class Nurse(Person):

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("\nNurse Details")
        print("Name :", self.name)
        print("Department :", self.department)


# ------------------ Polymorphism ------------------
def show_details(person):
    person.display()


# ------------------ Main Program ------------------
patient = Patient("Harish", 22, "Fever")
doctor = Doctor("Sahith", "Cardiologist")
nurse = Nurse("Srekanth", "Emergency")

# Encapsulation
patient.set_disease("Dengue")

# Polymorphism
show_details(patient)
show_details(doctor)
show_details(nurse)