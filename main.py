# Shehab Tarek 320220099 group 2 section 5
import re
print("you can use + - / * % operators only for now\n")
text = input("Write your mathematicial equation:")

text = text.replace(" ", "")# removing all spaces from the equation

def function():
    global text
    search = re.search("\d+",text) # search for digits 0 ~ 9
    if search:
        num = int(search.group(0))
        search2 = re.search("\W",text) # search for operators like + - / * %
        if search2:
            operator = search2.group(0)
            # removing the first few digits and first operator from the text
            text = text[search2.span(0)[1]:]

            if operator == '+':
                return num + function()
            elif operator == '-':
                return num - function()
            elif operator == '*':
                return num * function()
            elif operator == '/':
                return num / function()
            elif operator == '%':
                return num % function()
            else: # none of defined operators were found
                return num
        else: # no operator found after digits
            return num

print(function())