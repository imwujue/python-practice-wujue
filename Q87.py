class student:
    code = 0
    name = ""
    def input(self):
        self.code = int(input("code:"))
        self.name = (input("name:"))

if __name__ == '__main__':
    s1 = student()
    s1.input()
    print(s1.name,s1.code)