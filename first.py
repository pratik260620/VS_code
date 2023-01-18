class Customer():
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def intro(self):
        print(self.name, self.age)


C1= Customer('Pratik',32)
C2= Customer('Priya',29)
# print(C1)
# print(C2)
list=[C1,C2]
print(list)
for i in list:
     i.intro()


print("hiiiii")