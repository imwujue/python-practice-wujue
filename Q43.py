class static:
    staticVar = 0
    def varfunc(self):
        self.staticVar += 1
        print(self.staticVar)

if __name__ == '__main__':
    var = static()
    for i in range(3):
        var.varfunc()