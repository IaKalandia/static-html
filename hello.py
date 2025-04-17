# 1.say_hello
def say_hello():
   return "Hello, World!"

# 2. addition
def additon(a,b):
    return a+b

# 3.subtraction
def subtraction(a,b):
    return a-b

# 4. multiplication
def multiplication(a,b):
    return a*b

# 5. division
def division(a,b):
    return a/b

# 6. reverse_string
def reverse_string(string):
    return string[::-1]

# 7. reverse_string_using_loop
def reverse_string_using_loop(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string

# 8. add input function to the previous program
def reverse_string_using_input():
    string = input("Enter a string: ")
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string

#main function
if __name__ == "__main__":
    print(say_hello())
    print(additon(1,2))
    print(subtraction(1,2))
    print(multiplication(1,2))
    print(division(1,2))
    print(reverse_string("hello"))
    print(reverse_string_using_loop("hello"))
    print(reverse_string_using_input())

   

