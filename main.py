# Shehab Tarek 320220099
import re

text = input("Write your mathematicial equation:")

print(re.search("\d+",text).group(0))