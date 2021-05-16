import xlrd 
from analizadorLexico import l_tok

class node:
  def __init__(self, data, id, parent,value): 
    self.data = data
    self.id = id
    self.parent = parent
    self.childs = []
    self.value = value

def print_tree(root):

    if root:
      if root.parent:
        #print("primer if")
        print(root.data + "_" + str(root.id) + "(" + root.parent.data + "_" + str(root.parent.id) +")\n")
      else:
        #print("segundo if")
        print(root.data + "_" + str(root.id) + "\n")
      for child in root.childs:
        print_tree(child)

stack_nodes = []

def print_stack_nodes(stack_nodes):
  print("STACK_NODE: ****************************************************")
  for element in stack_nodes:
    print(element.data + "_" + str(element.id) + ", ", end = '') 
  print()

def get_dot(root,fi):
  
  if root:             
      for child in root.childs:
        #print(root.data + "_" + str(root.id) + " -> " + child.data + "_" + str(child.id)  )
        lin = root.data + "_" + str(root.id) + " -> " + child.data + "_" + str(child.id) + ";\n"
        fi.write(lin)
        get_dot(child,fi)

##########################################################################
  
gbl_counter_id = 0



####INICIO OBTENIENDO MATRIZ### 
loc = ("C:\\Users\\Katherine Bravo\\Desktop\\Compilador\\Compilador\\tablas2.xls") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

nonTerminal = []
for i in range(1,sheet.nrows): 
  nonTerminal.append(sheet.cell_value(i, 0))

#print(nonTerminal)

Terminal = []
for i in range(1,sheet.ncols): 
  Terminal.append(sheet.cell_value(0, i))
#print(Terminal)

L=[]
for row in range (1,sheet.nrows):
    _row = []
    for col in range (1,sheet.ncols):
        whiteSpaceRegex = " "
        contenido = sheet.cell_value(row,col)
        contenido = contenido[1:] #temporal
        words = []
        words = contenido.split(whiteSpaceRegex)
        _row.append(words)
    L.append(_row)

####FIN OBTENIENDO MATRIZ### 

#To evaluate int * ( int + int )
B = ["INT","MULT","GROUP_L","INT","SUM","INT","GROUP_R","$"]
#To evaluate int * 
#A = ['ent', 'ID', '<', '>', '{', 'dec', 'ID', '=', 'ID', ';', '}', '$']
st = "ent ID l_group r_group l_key dec ID equal ID com_separator ent ID com_separator para l_group ID lmayor ID hasta ID a_paso_de ID r_group l_key r_key r_key lsonido ID l_group r_group l_key ent ID equal ID com_separator ent ID com_separator r_key $"
#A = list(st.split(" "))
A= l_tok + [['$','$']]
print(A)
#print(L[0][0][0])

#if( L[0][1]):
#  print("Esta vacio")
#if( L[0][0]):
#  print("no Esta vacio")

def estaVacio(lis):
  if(lis == ['']):
    return True
  else:
    return False

def getNum(arg):
  if(arg not in Terminal):
    return nonTerminal.index(arg)
  else:
    return Terminal.index(arg)

#print(nonTerminal(L[0][0][0])) retorna 2 -> T

flag=True

aux = ["S"]

f = open ("parserUnion.dot","+w")

f.write("digraph {\n")

##########################################################################
##########################################################################
root = node("S", gbl_counter_id, None, None)
stack_nodes.insert(0,root)
gbl_counter_id += 1

print_tree(root)
print_stack_nodes(stack_nodes)
##########################################################################
##########################################################################

while(aux or A):
  if(not aux or not A):
    print("error")
    flag = False
    break

  if(aux[0]==A[0][0]):
    print("terminals...", " aux: ", aux, " A:", A), "\n"
    #print("Pop a",aux[0])
    aux.pop(0)
    A.pop(0)
    if len(stack_nodes) >= 1:
      stack_nodes.pop(0)
    #print(aux,"___",A,"\n")

  else:
    if(not estaVacio(L[getNum(aux[0])][getNum(A[0][0])]) and aux[0]!=A[0][0] and L[getNum(aux[0])][getNum(A[0][0])] != ["EMPTY"]):

      ##########################################################################
      ##########################################################################

      new_production = L[getNum(aux[0])][getNum(A[0][0])] 
      print("new_production:", new_production)
      father = stack_nodes[0]
      stack_nodes.pop(0)
      for element in reversed(new_production):
        nod = node(element, gbl_counter_id, father, A[1])
        stack_nodes.insert(0,nod)
        gbl_counter_id += 1
        father.childs.append(nod)

      
      print("TREE: *********************************************************")
      print_tree(root)
      print_stack_nodes(stack_nodes)
      print("finish: *******************************************************")
      ##########################################################################
      ##########################################################################

      
      pri = aux.pop(0)
      aux = L[getNum(pri)][getNum(A[0][0])] + aux
      print("->",pri,"-",A[0][0],":",L[getNum(pri)][getNum(A[0][0])], "stack:", aux, "\n\n\n")
      print(aux,"___",A,"\n")

      

    elif(L[getNum(aux[0])][getNum(A[0][0])] == ["EMPTY"]):
      aux.pop(0)
      stack_nodes.pop(0)

    elif(estaVacio(L[getNum(aux[0])][getNum(A[0][0])])):
      print("error:")
      flag = False
      break


if(flag):
  print("Si pertenece al lenguaje")
else:
  print("No pertenece al lenguaje")

print("PROCESSING DOT .....")
get_dot(root,f)
f.write("}") 
f.close()

print(l_tok)
