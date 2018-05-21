class Student:
    name = ''
    age = 0
    students = []

    def read_file(self):
        try:
            fr = open("students.txt", "r")
            data = fr.readlines()
            for line in data:
                words = line.split()
                self.students.append(words[0])
                self.students.append(words[1])
            fr.close()
        except Exception:
            print('cant read file')

    def write_file(self):
        fw = open('students.txt', 'a')
        print(self.name + ' ' + self.age, file=fw)
        fw.close()


if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    student = Student()

    while True:
        addMore = input('Want to add more y/n : ')
        if addMore == 'y':
            student.name = input('Enter student name : ')
            student.age = int(input('Enter student age : '))
            student.write_file()
        else:
            break
    student.read_file()
    print(student.students)
