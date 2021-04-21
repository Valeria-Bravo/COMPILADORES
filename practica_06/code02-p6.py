import re
aux = """hola 21-05-1999"""

aux2 =r"[\d+\-+\d+\-+\d]{10}"
match = re.findall(aux2,aux)
print(match)