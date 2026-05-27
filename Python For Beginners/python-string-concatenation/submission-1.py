def concatenate(s1: str, s2: str) -> str:
    length1 = len(s1)
    length2 = len(s2)

    value= length1+length2

    if value <= 10:
        return s1+s2
    else:
        return ("Too long!")




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
