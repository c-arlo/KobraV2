# Generated from KobraV2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from src.parser.KobraV2Parser import KobraV2Parser
else:
    from src.parser.KobraV2Parser import KobraV2Parser

# This class defines a complete generic visitor for a parse tree produced by KobraV2Parser.

class KobraV2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by KobraV2Parser#programa.
    def visitPrograma(self, ctx:KobraV2Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#instruccion.
    def visitInstruccion(self, ctx:KobraV2Parser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#bloque.
    def visitBloque(self, ctx:KobraV2Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#declaracion.
    def visitDeclaracion(self, ctx:KobraV2Parser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#asignacion.
    def visitAsignacion(self, ctx:KobraV2Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#impresion.
    def visitImpresion(self, ctx:KobraV2Parser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#si_stmt.
    def visitSi_stmt(self, ctx:KobraV2Parser.Si_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#while_stmt.
    def visitWhile_stmt(self, ctx:KobraV2Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#for_stmt.
    def visitFor_stmt(self, ctx:KobraV2Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#asignacion_for.
    def visitAsignacion_for(self, ctx:KobraV2Parser.Asignacion_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#expresion_stmt.
    def visitExpresion_stmt(self, ctx:KobraV2Parser.Expresion_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Variable.
    def visitVariable(self, ctx:KobraV2Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Flotante.
    def visitFlotante(self, ctx:KobraV2Parser.FlotanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#OpIgualdad.
    def visitOpIgualdad(self, ctx:KobraV2Parser.OpIgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#OpRelacional.
    def visitOpRelacional(self, ctx:KobraV2Parser.OpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Entero.
    def visitEntero(self, ctx:KobraV2Parser.EnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#OpMultiplicativa.
    def visitOpMultiplicativa(self, ctx:KobraV2Parser.OpMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Parentesis.
    def visitParentesis(self, ctx:KobraV2Parser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#OpLogica.
    def visitOpLogica(self, ctx:KobraV2Parser.OpLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Cadena.
    def visitCadena(self, ctx:KobraV2Parser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#Booleano.
    def visitBooleano(self, ctx:KobraV2Parser.BooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KobraV2Parser#OpAditiva.
    def visitOpAditiva(self, ctx:KobraV2Parser.OpAditivaContext):
        return self.visitChildren(ctx)



del KobraV2Parser