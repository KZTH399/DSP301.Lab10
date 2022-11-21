import re

str='''Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores.'''

#Type your answer here.

emails=re.findall('(\w{8})', str)


print(emails)
