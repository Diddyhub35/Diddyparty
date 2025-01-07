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
# clg id & dept = unparamerised 
class college :
    def info_1 (self , clg_name , clg_addr ):
        print ("the name of the college is :" , clg_name)
        print ("the college address :" , clg_addr)

    def info_2 (self):
        self.clg_id = 10213
        self.clg_dept = "artificial intelligence "
        print ("the college id :", self.clg_id ,end = " " )
        print ("the department is :", self.clg_dept)

obj = college ()
obj.info_1("pgmcoe ", "wagholi")
obj.info_2()
