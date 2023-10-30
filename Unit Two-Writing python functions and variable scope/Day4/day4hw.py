def string_middle(string):
    return string[1:len(string)-1]




print(string_middle("hurican"))




def first_last(string):
    first=string[0:1]
    last=string[len(string)-1:len(string)]
    return first+last

print(first_last("hello"))
