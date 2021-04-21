import re

aux = """hola como estas
todo bien"""

aux2 =r'[\s+(\s*) | \n]'

match = re.findall(aux2,aux)
print(match)