from antlr4 import *
from gLexer import gLexer  # Lexer generado a partir de g.g4
from gParser import gParser  # Parser generado a partir de g.g4

# Implementación de las funciones MAP y FILTER en Python
def MAP(func, iterable):
    return list(map(func, iterable))

def FILTER(cond, iterable):
    return list(filter(cond, iterable))

# Definición de funciones para las pruebas
def eval_function(name, args):
    if name == 'doble':
        return lambda x: x * 2
    elif name == 'par':
        return lambda x: x % 2 == 0
    return None

# Listener para recorrer el árbol de parseo y ejecutar las funciones
class EvalListener(ParseTreeListener):
    def exitMapStmt(self, ctx):
        func_name = ctx.function().getText()
        iterable = eval(ctx.iterable().getText())  # Convierte la lista a un objeto Python
        func = eval_function(func_name, [])
        result = MAP(func, iterable)
        print("Resultado MAP:", result)

    def exitFilterStmt(self, ctx):
        func_name = ctx.function().getText()
        iterable = eval(ctx.iterable().getText())  # Convierte la lista a un objeto Python
        cond = eval_function(func_name, [])
        result = FILTER(cond, iterable)
        print("Resultado FILTER:", result)

# Función principal para ejecutar el parser y el listener con entrada desde un archivo de texto
def main(input_file):
    # Lee el archivo de texto
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Crea el lexer y el parser usando la entrada del archivo
    lexer = gLexer(InputStream(input_data))  # Lee desde el archivo de texto
    stream = CommonTokenStream(lexer)
    parser = gParser(stream)
    tree = parser.program()

    # Crea un listener para evaluar el árbol
    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    # Asegúrate de que el programa recibe el nombre del archivo como argumento
    import sys
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo.txt>")
    else:
        main(sys.argv[1])

