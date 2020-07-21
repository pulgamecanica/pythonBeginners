def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter Temperature: "))
print(type(user_input), user_input)
print(weather_condition(user_input))

def greetings(name):
    return "Hello %s" % name + "!"

print(greetings(input("Enter your name: ")))

name = input("Enter your name: ")
age = int(input("Enter your age: "))

message1 = "Hello %s, you are %s years old!" % (name, age)
message2 = "Hello {}, you are {} years old!".format(name, age)

print(message1)
print(message2)