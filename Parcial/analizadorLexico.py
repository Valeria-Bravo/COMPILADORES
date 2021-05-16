import ply.lex as lex
reserved= {
    'main':'main', #puede que lo quitemos
    'int':'int',
    'bool':'bool',
    'return': 'return',
    'func':'func',
    'string':'string',
    'float':'float',
    'char': 'char',
    'if': 'if',
    'else': 'else', 
    'for': 'for' , 
    'while':'while',
    'show' : 'show',
    'catch' : 'catch',
    'size' : 'size'
}
tokens=[ 'numbers','decimal','suma', 'resta', 'multip', 'div','and',
            'ipar', 'dpar', 'or', 'dist',
         'illav','dllav','igual', 'mayor','menor', 'mayoreq','menoreq','coma','ptocoma','boolean', 'mod',
          'comment','var','varstr','varch','digual','comentario2','id']+ list(reserved.values())

t_suma=r'\+'
t_resta=r'-'
t_multip=r'\*'
t_div=r'/'
t_digual=r'\=='
t_ipar=r'\('
t_dpar=r'\)'
t_illav=r'\{'
t_dllav=r'\}'
t_igual=r'\='
t_mayor=r'\>'
t_menor=r'\<'
t_mayoreq=r'\>='
t_menoreq=r'\<='
t_ptocoma=r'\;'
t_or=r'\|\|'
t_dist=r'\!='
t_and=r'\&&'
t_coma=r'\,'
t_mod=r'\%'
t_varstr = r'(\"\w*\")'
t_varch = r'(\"\w\")' #problemita con estos dos
t_comment = r'(\#\w*(.|,)*(\s)*\w*)*\n' 
t_var = r'\"((\s)*\w*(\s)*\w*)*\"'

#\$ [a-zA-Z_][a-zA-Z_0-9]*
#(\$\w*(.|,)*(\s)*\w*)*\n
def t_numbers(t):
    r'[+-]?([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?'
    t.value = float(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_boolean(t):
    r'true|false'
    return t 

def t_id(t): 
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  #t.type = reserved.get(t.value.lower(),'id')  
  t.type = reserved.get(t.value, 'id') 
  return t

#def t_var(t):
  #r' \"[a-zA-Z_][a-zA-Z_0-9]*\"'
  
 # return t

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

#def t_comment(t):
    #r'$[a-zA-Z_][a-zA-Z_0-9]'
   # t.lexer.lineno += 1
  
def t_comentario2(t):
     r'/\*(.|\n)*?\*/'
     t.lexer.lineno += t.value.count('\n')

t_ignore  = ' \t'


fp = open("C:\\Users\\Katherine Bravo\\Desktop\\Compilador\\Compilador\\union_examples.txt")
cadena = fp.read()
print(cadena)
fp.close()

analizador = lex.lex()

analizador.input(cadena)
l_tok=[]
while True:
	uni_tok=[]
	tok = analizador.token()
	if not tok : break
	print (tok)
	uni_tok.append(tok.type)
	uni_tok.append(tok.value)
	l_tok.append(uni_tok)

print(l_tok)