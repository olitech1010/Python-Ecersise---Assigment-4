from shopping_cart import ShoppingCart, Item
from student import Student

# creating the ShoppinCart object in the main    
cart = ShoppingCart()

# adding some items to the cart
item1 = Item("beans", 5.00)
item2 = Item("gari", 1.00)
item3 = Item("plantain", 4.00)
item4 = Item("egg", 3.00)
cart.addItem(item1)
cart.addItem(item2)
cart.addItem(item3)
cart.addItem(item4)

# removing an Item from the cart
cart.removeItem(item4)

# getting the total price of all items in the cart
totalPrice = cart.getTotalPrice()

# printing out the total price
print("Total price of items in the cart: GH¢" + str(totalPrice))

## STUDENT CLASS
#setting student object
student = Student()

#setting student name, ID, 
student.setName("Clement Mensah")
student.setStudentID("10945134")

# adding courses to courselist
student.addCourse("DCIT201")
student.addCourse("DCIT203")
student.addCourse("DCIT205")
student.addCourse("DCIT207")
student.addCourse("DCIT209")
student.addCourse("UGRC210")

#print sutdent name and courses
print("Student Name: ", student.getName())
print("Student ID: ", student.getStudentID())
print("Student Course List: ")
student.displayCourses()

#removing some courses 
student.removeCourse("DCIT207")

#printing updated courselist
print("Updated course lists: ")
student.displayCourses()

