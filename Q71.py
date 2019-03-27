class student:
    name = ""
    age = 0
    score = 0

    def input(self):
        self.name = input("name:")
        self.age = int(input("age:"))
        self.score = int(input("score:"))

    def output(self):
        print("name:",self.name)
        print("age:",self.age)
        print("score:",self.score)

if __name__ == '__main__':
    student_list = []
    for i in range(5):
        student_list.append(student())
    for i in range(5):
        student_list[i].input()
    for i in range(5):
        student_list[i].output()