import sys
from antlr4 import *
from KobraV2Lexer import KobraV2Lexer
from KobraV2Parser import KobraV2Parser
from KobraCompiler import KobraToPythonVisitor


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_input.txt>")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace('.txt', '.py')

    # 1. Leer input
    input_stream = FileStream(input_file, encoding='utf-8')

    # 2. Lexer
    lexer = KobraV2Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 3. Parser
    parser = KobraV2Parser(stream)
    tree = parser.programa()  # 'programa' es la regla raiz

    # Verificar errores de sintaxis
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores de sintaxis encontrados. No se generó código.")
        return

    # 4. Transpilación (Visitor)
    visitor = KobraToPythonVisitor()
    python_code = visitor.visit(tree)

    # 5. Guardar Output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(python_code)

    print(f"Transpilación exitosa! Archivo generado: {output_file}")


if __name__ == '__main__':
    main()