class Student: # назва класу
    def __init__(self, name, surname, age, average_score=100):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_score):
        self.average_score = new_score
    
    def tell_about_yourself(self):
        return (f"Студент: {self.name} {self.surname}, Вік: {self.age}, "
                f"Середній бал: {self.average_score}")


student1 = Student("Anna", "Hurfinkel", "28", 55)

student1.change_average_score(80)

print(student1.tell_about_yourself())
