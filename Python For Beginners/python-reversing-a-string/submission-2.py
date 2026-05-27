def reverse_string(input_string: str) -> str:
    value=len(input_string)
    return (input_string[value::-1])

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
