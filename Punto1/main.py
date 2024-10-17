import sys
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitor import gVisitor

class EvaluadorComplejo(Visitor):
    def visitOperacionBinaria(self, ctx):
        izquierda = self.visit(ctx.expr(0))
        derecha = self.visit(ctx.expr(1))
        operador = ctx.op.text
        if operador == '+':
            return izquierda + derecha
        elif operador == '-':
            return izquierda - derecha

    def visitOperacionMultiplicacionDivision(self, ctx):
        izquierda = self.visit(ctx.expr(0))
        derecha = self.visit(ctx.expr(1))
        operador = ctx.op.text
        if operador == '*':
            return izquierda * derecha
        elif operador == '/':
            return izquierda / derecha

    def visitComplejo(self, ctx):
        return complex(ctx.getText())

    def visitReal(self, ctx):
        return float(ctx.getText())

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

def main():
    input_stream = InputStream(input("Introduce la expresión: "))
    
    lexer = gLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gParser(stream)
    
    tree = parser.expr()  # Comienza la evaluación a partir de la regla 'expr'
    
    evaluador = EvaluadorComplejo()
    resultado = evaluador.visit(tree)
    
    print(f"Resultado: {resultado}")

if __name__ == '__main__':
    while(True):
        main()

