class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Name: {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


    def get_info(self):
        return f"Student Name: {self._name}, ID: {self.student_id}"

people = [Person("Ivan"), Student("Zarina", "1633")]

for p in people:
    print(p.get_info())

person = Person("Ivan")
student = Student("Zarina", "1633")

print(person.get_info())
print(student.get_info())
