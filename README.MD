### Requisitos previos

1. **ANTLR**: Asegúrate de tener ANTLR instalado en tu sistema.
   - [Guía de instalación de ANTLR](https://www.antlr.org/download.html)
   
2. **Python**: Versión 3.x.
    x
3. **Instalar el runtime de ANTLR para Python**:
   ```bash
   pip install antlr4-python3-runtime
   ```
### Uso del PUNTO 1
**Genera el lexer y el parser:**
```bash
    antlr4 -Dlanguage=Python3 -visitor g.g4
```
**Ejecutar el programa** desde la terminal, proporcionando el archivo de entrada:
   ```bash
   python3 main.py
   ```
**Introduce expresiones con reales o imaginarios (a+bj) de la forma.** 
Ejemplo:
```bash
   (2+3j)+(4-2j)
```

### Uso del PUNTO 2
Ejecuta el siguiente comando para generar el lexer y el parser en Python:
   ```bash
   antlr4 -Dlanguage=Python3 g.g4
   ```

1. **Crear un archivo de entrada (`input.txt`)** con las instrucciones que quieres procesar. Ejemplo:
   ```txt
   MAP(doble, [1, 2, 3, 4])
   ```
   
   ```txt
   FILTER(multiple, [1, 2, 3, 4])
   ```

2. **Ejecutar el programa**
   ```bash
   python3 main.py input.txt
   ```

3. **Salida esperada**:
   El programa procesará las instrucciones y mostrará los resultados en la terminal, por ejemplo:
   ```bash
   Resultado MAP: [2, 4, 6, 8]
   ```
   
   ```bash
   Resultado FILTER: [2, 4]
   ```
### Funciones disponibles
- `doble`: Multiplica cada elemento por 2.
- `par`: Filtra los múltiplos de 2.

### Uso del PUNTO 3
Ejecuta el siguiente comando para generar el lexer y el parser en Python:
   ```bash
   antlr4 -Dlanguage=Python3 g.g4
   ```
1. **Crear un archivo de entrada (`input.txt`)**. Ejemplo:
   ```txt
   MAP(doble, [1, 2, 3, 4])
   ```
2. **Ejecutar el programa**
   ```bash
   python3 main.py input.txt
   ```
3. **Salida esperada**:
   El programa procesará las instrucciones y mostrará la grafica de la transformada.

