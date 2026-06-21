class ParentClass:
    def Print(self):
        print('Hello , world!')
class ChildClass(ParentClass):
    def someNewMethod(self):
        print("ParentClass objects don't have this method. ")
class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Only GrandChild Object have this method.')
print('Create a ParentClass object and call its methods: ')
parent=ParentClass()
parent.Print()

print(' Create a ChildClass object and  call its method.')
child=ChildClass()
child.Print()
child.someNewMethod()

print(' Create a GrandChild object and call its method.')
GrandChild=GrandchildClass()
GrandChild.anotherNewMethod()
GrandChild.someNewMethod()
GrandChild.Print()

print("Error!")
ParentClass.someNewMethod()
