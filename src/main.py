import sys
from antlr4 import *
from src.lexer.KobraV2Lexer import KobraV2Lexer
from src.parser.KobraV2Parser import KobraV2Parser
from src.semantic.KobraCompiler import KobraToPythonVisitor


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_input.txt>")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace('.txt', '.py')

    # 1. Leer input
    input_stream = FileStream(input_file, encoding='utf-8')

    # 2. lexer
    lexer = KobraV2Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    stream.fill()
    print("\n--- Tokens identificados ---")
    for token in stream.tokens:
        print(token.text)
    print("\n")

    # 3. parser
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