class Employee_details_collector_and_manager:
       
       #This class will accept the details of the employees and then display it as the user wishes.
       
       def __init__(self,employee_name,employee_id,
                    employee_job,employee_salary,
                    employee_department_number):
              
              #This method will initialize all the values taken from the users.

              self.employee_name = employee_name
              self.employee_id = employee_id
              self.employee_job = employee_job
              self.employee_salary = employee_salary
              self.employee_department_number = employee_department_number

       def display_employee_details(self):
              
              #This method will display all the details which were taken by the user. 
              
              print(f"The name of the employee is {self.employee_name}")
              print(f"The Id of the employee if {self.employee_id}")
              print(f"The job of the employee is {self.employee_job}")
              print(f"The salary of the employee is {self.employee_salary}")
              print(f"The department number of the employee is {self.employee_department_number}")

class Emplyoee_net_salary_calculator:
       
       #This class will take the basic salary from the use rand then calculate the net salary.
       
       def __init__(self,basic_salary):
              
              #This method will initialize the basic salary taken from the users.

              self.basic_salary = basic_salary

       def net_salary_calculator(self):

              #This method will calculate the net salary of the user.

              self.income_tax = self.basic_salary + 30/100
              self.sales_tax = self.basic_salary + 20/100
              self.service_tax = self.basic_salary + 15/100
              self.net salary = self.basic_salary +  self.sales_tax + self.service_tax + self.income_tax

              print(f"The net salary of the employee is {self.net salary}")

employee_details_object = Employee_details_collector_and_manager(input("Enter employee name: "),input("Enter employee id: "),input("Enter employee job: "),input("Enter employee salary: "),input("Enter employee department number: "))
employee_net_salary_object = Emplyoee_net_salary_calculator(int(input("Enter basic salary of the user:")))

while True:
                                                            
       #Adding user options.
       
       print("1.Emplyoee details")
       print("2.Calculate net salary")
       print("3.Quit")

       #Taking user options.
       user_option = int(input("Enter any option from above: "))

       if user_option == 1:
              employee_details_object.display_employee_details()      #Displays user details.

       elif user_option == 2:
              employee_net_salary_object.net_salary_calculator()      #Calculates net salary

       elif user_option == 3:
              break                                                                                    # Quits from the menu

       else:
              print("Enter correct options")                           #An option is entered wrong
                            
              
              
