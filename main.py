# Shehab Tarek 320220099    
import re
text = input("Write your mathematicial equation:")

# searches for digits
search = re.search("\d+",text)
digit_from_text = search.group(0)

# removing the first digits from the thing
text = text[search.span(0)[1]:]
print(text)