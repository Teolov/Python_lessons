class Dogs():
    def __init__(self, name_loc):
        # print('start class Dogs')
        self.num = 9
        # print(self.num)
        # print(name_loc)
        self.name = name_loc
        self.eat_num = 0
    def run(self):
        print('run run run')
        # self.eat()
    def eat(self, number = 2):
        self.eat_num += number
        
    

dog_sharik = Dogs('Sharik')
# print(type(dog_sharik))
# print(dog_sharik.num)

# dog_sharik.run()

dog_sharik.eat(9)
print(dog_sharik.eat_num)




