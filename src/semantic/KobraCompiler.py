from src.parser.KobraV2Parser import KobraV2Parser
from src.semantic.KobraV2Visitor import KobraV2Visitor


class KobraToPythonVisitor(KobraV2Visitor):
    def __init__(self):
        self.indent_level = 0
        self.output = ""

    def add_line(self, line):
        # Agrega indentación y la linea
        self.output += ("    " * self.indent_level) + line + "\n"

    def visitPrograma(self, ctx):
        self.add_line("# -*- coding: utf-8 -*-")

        self.add_line("# Codigo generado desde KobraV2")
        self.add_line("import sys")
        self.add_line("")

        # --- HELPER PARA DIVISION ---
        # Inyectamos esta funcion para manejar division entera vs flotante
        helper_code = """
def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b
"""
        # Añadimos el helper al output sin indentar (nivel 0)
        self.output += helper_code + "\n"

        # Visitamos el resto de los hijos (las instrucciones)
        self.visitChildren(ctx)

        # --- ¡ESTA ES LA LINEA QUE FALTABA! ---
        return self.output

    def visitDeclaracion(self, ctx):
        # Kobra: INT x = 10; -> Py: x = 10
        # Ignoramos el tipo explicito en la traduccion simple (Python es dinamico)
        var_name = ctx.ID().getText()
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.add_line(f"{var_name} = {valor}")
        else:
            # Si solo declara sin valor (INT x;), inicializamos en None
            self.add_line(f"{var_name} = None")
        return None

    def visitAsignacion(self, ctx):
        var_name = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.add_line(f"{var_name} = {valor}")
        return None

    def visitImpresion(self, ctx):
        valor = self.visit(ctx.expresion())
        self.add_line(f"print({valor})")
        return None

    def visitSi_stmt(self, ctx):
        condicion = self.visit(ctx.expresion())
        self.add_line(f"if {condicion}:")

        # Visitamos el bloque VERDADERO
        self.visit(ctx.bloque(0))  # Primer bloque

        # Si hay SINO
        if ctx.bloque(1):
            self.add_line("else:")
            self.visit(ctx.bloque(1))
        return None

    def visitWhile_stmt(self, ctx):
        condicion = self.visit(ctx.expresion())
        self.add_line(f"while {condicion}:")
        self.visit(ctx.bloque())
        return None

    def visitFor_stmt(self, ctx):
        # Kobra: PARA (i=0; i<10; i=i+1) { ... }
        # Python: i=0; while i<10: ... i=i+1
        # Convertiremos el FOR de C en un WHILE de Python para facilitar la traduccion

        # 1. Inicialización (se imprime antes del ciclo)
        init_stmt = ctx.asignacion_for(0)
        var_init = init_stmt.ID().getText()
        val_init = self.visit(init_stmt.expresion())
        self.add_line(f"{var_init} = {val_init}")

        # 2. Condición
        condicion = self.visit(ctx.expresion())
        self.add_line(f"while {condicion}:")

        # Aumentamos indentacion para el cuerpo
        self.indent_level += 1

        # 3. Cuerpo del loop (extraemos las instrucciones del bloque manualmente)
        # El bloque tiene hijos, visitamos los hijos que sean instrucciones
        bloque_ctx = ctx.bloque()
        for child in bloque_ctx.getChildren():
            if isinstance(child, KobraV2Parser.InstruccionContext):
                self.visit(child)

        # 4. Actualización (al final del while)
        update_stmt = ctx.asignacion_for(1)
        var_update = update_stmt.ID().getText()
        val_update = self.visit(update_stmt.expresion())
        # Usamos add_line normal, ya tiene el indent_level aumentado
        self.add_line(f"{var_update} = {val_update}")

        self.indent_level -= 1
        return None

    def visitBloque(self, ctx):
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    # --- EXPRESIONES ---
    # Retornan strings con el código de la expresión

    def visitParentesis(self, ctx):
        return f"({self.visit(ctx.expresion())})"

    def visitOpAditiva(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        return f"{left} {op} {right}"

    def visitOpMultiplicativa(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text

        if op == '/':
            return f"_kobra_div({left}, {right})"

        return f"{left} {op} {right}"

    def visitOpRelacional(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        return f"{left} {op} {right}"

    def visitOpIgualdad(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        # En Kobra '==' es igual a Python, pero si fuera distinto aquí se cambia
        return f"{left} {op} {right}"

    def visitOpLogica(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        # Traducir Y/O a and/or
        py_op = "and" if op == 'Y' else "or"
        return f"{left} {py_op} {right}"

    def visitVariable(self, ctx):
        return ctx.ID().getText()

    def visitEntero(self, ctx):
        return ctx.INT().getText()

    def visitFlotante(self, ctx):
        return ctx.FLOAT().getText()

    def visitCadena(self, ctx):
        return ctx.STRING().getText()

    def visitBooleano(self, ctx):
        val = ctx.BOOL_LIT().getText()
        return "True" if val == "VERDADERO" else "False"
