__author__ = 'Wise'

# Program clean all coments in Java or C++ code

fl = open('data.txt')

current_state = 0

result = ""

while 1:
    cha = fl.read(1)
    if not cha:
        break
    if current_state == 0:
        if cha == '"':
            current_state = 1
            result += cha
        elif cha == '/':
            current_state = 2
        elif cha == '\\':
            current_state = 6
            result += cha
        else:
            result += cha
    elif current_state == 1:
        if cha == '"':
            current_state = 0
            result += cha
        result += cha
    elif current_state == 2:
        if cha == '/':
            current_state = 3
        elif cha == '*':
            current_state = 4
        else:
            result += cha
    elif current_state == 3:
        if cha == '\n':
            current_state = 0
    elif current_state == 4:
        if cha == '*':
            current_state = 5
    elif current_state == 5:
        if cha == '/':
            current_state = 0
    elif current_state == 6:
        current_state = 0
        result += cha

print result

res = open("result.txt", 'w')
res.write(result)
res.close()
fl.close()