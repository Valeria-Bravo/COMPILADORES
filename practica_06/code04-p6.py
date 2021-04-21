import re 

aux = """hola func_hola"""

aux2=r"[[_a-zA-Z][_a-zA-Z0-9]]*"
match=re.findall(aux2,aux)
print(match)