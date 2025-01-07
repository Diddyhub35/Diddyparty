# OOPS_concepts
# class animal :
#     name = ""
#     age = ""
#     colour = ""

# obj=animal ()
# obj.name = "cat"
# obj.age = 13
# obj.colour = "red"

# print (obj.name)


# class employee :
#     employee_id =""
#     name =""
#     age =""
#     salary =""
#     dept =""

#     def type (self):
#         self.employee_id = 101
#         self.name = "aakash "
#         self.age = 42
#         self.salary = 45000
#         self.dept = "HR"
#         print ("name :",self.name , end = " ")
#         print ("age :",self.age , end = " ")
#         print ("salary :",self.salary , end = " ")
#         print ("department :",self.dept , end = " ")

# obj = employee()
# obj.type ()


# clg name & address parameterised 
# # clg id & dept = unparamerised 
# class college :
#     def info_1 (self , clg_name , clg_addr ):
#         print ("the name of the college is :" , clg_name)
#         print ("the college address :" , clg_addr)

#     def info_2 (self):
#         self.clg_id = 10213
#         self.clg_dept = "artificial intelligence "
#         print ("the college id :", self.clg_id ,end = " " )
#         print ("the department is :", self.clg_dept)

# obj = college ()
# obj.info_1("pgmcoe ", "wagholi")
# obj.info_2()


# inheritance :
# single inheritance 
class A :
    def info_1 (self):
        print ("this is parent class ")

class B (A):
    def info_2(self):
        print ("this is the child class ")

a = B()
a.info_1()
a.info_2()
print ("\n")




# multilevel inheritance 
class C (B):
    def info_3(self):
        print ("this is the second level of inheritance ")

b = C()
b.info_1()
b.info_2()
b.info_3()
print ("\n")


# hierarchal inheritance & multiple inheritance
class P :
    def info_4(self):
        print ("this is another parent class")

class Q (A ,P):
    def info_5(self ):
        print ("this has multiple inheritances ")

c = Q()
c.info_1()
c.info_4()
c.info_5()
print ("\n")


#  hybrid inheritance:
class E (B , Q):
    def info_6(self):
        print (" this is the exapmle of hybrid inheritance ")

d = E()
d.info_1()
d.info_2()
d.info_4()
d.info_5()
d.info_6()
print ("\n")