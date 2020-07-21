# Function to get the mean in a comparable list
def mean(mylist):
    print("Started!!!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 6, 9, 2, 3]))
#*************************
# Conditionals Dictionaries and lists
def meanAllDo(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

student_grades = {"Marry": 9.1, "Simao": 8.8, "John": 7.5}
print("Dictionary: ",meanAllDo(student_grades))
print("List; ", meanAllDo([1, 4, 6, 9, 2, 3]))
#***********************+
x = 1
y = 3
if x > 3:
    print("x is grater than 3")
elif y > 3:
    print("y is grater than 3")
else:
    print("Dang BOY")

if x < 1 or y <= 3:
    print("We Won!!!")
