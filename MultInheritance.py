class A:
    def method_A(self):
        print("Method A from class A")

class B:
    def method_B(self):
        print("Method B from class B")

class C(A, B):
    def method_C(self):
        print("Method C from class C")

obj = C()
obj.method_A()
obj.method_B()
obj.method_C()
