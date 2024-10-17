import sys
import numpy as np
import matplotlib.pyplot as plt
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitor import gVisitor

# Diccionario para almacenar variables
variables = {}

# Definimos un rango de valores para t
t_values = np.linspace(-10, 10, 1000)

# Visitor para evaluar expresiones
class FourierVisitor(gVisitor):
    
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        variables[var_name] = value
        print(f"{var_name} asignado.")
        return value

    def visitFftStatement(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in variables:
            signal = variables[var_name]
            fft_result = self.calculate_fft(signal)
            print(f"Transformada de Fourier de {var_name}:")
            self.plot_fft(fft_result)
        else:
            raise Exception(f"Variable '{var_name}' no definida.")
    
    def calculate_fft(self, signal):
        fft_result = np.fft.fft(signal)
        return fft_result

    def plot_fft(self, fft_result):
        freqs = np.fft.fftfreq(len(fft_result), t_values[1] - t_values[0])
        plt.plot(freqs, np.abs(fft_result))
        plt.title("Transformada de Fourier")
        plt.xlabel("Frecuencia")
        plt.ylabel("Magnitud")
        plt.grid()
        plt.show()

    def visitRectangularPulse(self, ctx):
        T = self.visit(ctx.expr(1))
        result = np.array([1 if abs(t) <= T / 2 else 0 for t in t_values])
        print(f"Pulso rectangular con T = {T}")
        return result

    def visitTriangularPulse(self, ctx):
        T = self.visit(ctx.expr(1))
        result = np.array([(1 - abs(t) / T) if abs(t) <= T else 0 for t in t_values])
        print(f"Pulso triangular con T = {T}")
        return result

    def visitSignFunction(self, ctx):
        result = np.array([1 if t > 0 else -1 for t in t_values])
        print("Función signo")
        return result

    def visitUnitStepFunction(self, ctx):
        result = np.array([1 if t >= 0 else 0 for t in t_values])
        print("Función escalón unitario")
        return result

    def visitDiracDelta(self, ctx):
        result = np.zeros_like(t_values)
        result[np.abs(t_values) < 1e-6] = np.inf  # Aproximación de la delta de Dirac
        print("Función delta de Dirac (aproximada)")
        return result

    def visitCosineFunction(self, ctx):
        omega = self.visit(ctx.expr(0))
        result = np.cos(omega * t_values)
        print(f"Función coseno con ω = {omega}")
        return result

    def visitSineFunction(self, ctx):
        omega = self.visit(ctx.expr(0))
        result = np.sin(omega * t_values)
        print(f"Función seno con ω = {omega}")
        return result

    def visitAddition(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSubtraction(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitMultiplication(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDivision(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right

    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.expr(0))

    def visitInteger(self, ctx):
        return int(ctx.getText())

    def visitFloat(self, ctx):
        return float(ctx.getText())

    def visitVariableReference(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in variables:
            return variables[var_name]
        raise Exception(f"Variable '{var_name}' no está definida.")

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')  # Especificar la codificación UTF-8
    lexer = gLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gParser(stream)
    tree = parser.program()

    visitor = FourierVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)

