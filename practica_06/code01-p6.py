import re
aux = """hola 14.1946 como estas 15.6785 y 10.1245"""
aux2 =r"[\d+(\.\d*)]{7}"

match = re.findall(aux2,aux)
print(match)   