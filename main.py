# Shehab Tarek 320220099    
import re
text = input("Write your mathematicial equation:")

def function():
    global text
    search = re.search("\d+",text) # search for digits
    if search:
        num = search.group(0)
        search2 = re.search("\W",text) # search for operator that are after digits like + - / * %
        if search2:
            operator = search2.group(0)
            # removing the first digits from the text
            text = text[search2.span(0)[1]:]
            print(text)
            function()

function()