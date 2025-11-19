# Generated from KobraV2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KobraV2Parser import KobraV2Parser
else:
    from KobraV2Parser import KobraV2Parser

# This class defines a complete listener for a parse tree produced by KobraV2Parser.
class KobraV2Listener(ParseTreeListener):

    # Enter a parse tree produced by KobraV2Parser#programa.
    def enterPrograma(self, ctx:KobraV2Parser.ProgramaContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#programa.
    def exitPrograma(self, ctx:KobraV2Parser.ProgramaContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#instruccion.
    def enterInstruccion(self, ctx:KobraV2Parser.InstruccionContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#instruccion.
    def exitInstruccion(self, ctx:KobraV2Parser.InstruccionContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#bloque.
    def enterBloque(self, ctx:KobraV2Parser.BloqueContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#bloque.
    def exitBloque(self, ctx:KobraV2Parser.BloqueContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#declaracion.
    def enterDeclaracion(self, ctx:KobraV2Parser.DeclaracionContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#declaracion.
    def exitDeclaracion(self, ctx:KobraV2Parser.DeclaracionContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#asignacion.
    def enterAsignacion(self, ctx:KobraV2Parser.AsignacionContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#asignacion.
    def exitAsignacion(self, ctx:KobraV2Parser.AsignacionContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#impresion.
    def enterImpresion(self, ctx:KobraV2Parser.ImpresionContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#impresion.
    def exitImpresion(self, ctx:KobraV2Parser.ImpresionContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#si_stmt.
    def enterSi_stmt(self, ctx:KobraV2Parser.Si_stmtContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#si_stmt.
    def exitSi_stmt(self, ctx:KobraV2Parser.Si_stmtContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#while_stmt.
    def enterWhile_stmt(self, ctx:KobraV2Parser.While_stmtContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#while_stmt.
    def exitWhile_stmt(self, ctx:KobraV2Parser.While_stmtContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#for_stmt.
    def enterFor_stmt(self, ctx:KobraV2Parser.For_stmtContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#for_stmt.
    def exitFor_stmt(self, ctx:KobraV2Parser.For_stmtContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#asignacion_for.
    def enterAsignacion_for(self, ctx:KobraV2Parser.Asignacion_forContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#asignacion_for.
    def exitAsignacion_for(self, ctx:KobraV2Parser.Asignacion_forContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#expresion_stmt.
    def enterExpresion_stmt(self, ctx:KobraV2Parser.Expresion_stmtContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#expresion_stmt.
    def exitExpresion_stmt(self, ctx:KobraV2Parser.Expresion_stmtContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Variable.
    def enterVariable(self, ctx:KobraV2Parser.VariableContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Variable.
    def exitVariable(self, ctx:KobraV2Parser.VariableContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Flotante.
    def enterFlotante(self, ctx:KobraV2Parser.FlotanteContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Flotante.
    def exitFlotante(self, ctx:KobraV2Parser.FlotanteContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#OpIgualdad.
    def enterOpIgualdad(self, ctx:KobraV2Parser.OpIgualdadContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#OpIgualdad.
    def exitOpIgualdad(self, ctx:KobraV2Parser.OpIgualdadContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#OpRelacional.
    def enterOpRelacional(self, ctx:KobraV2Parser.OpRelacionalContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#OpRelacional.
    def exitOpRelacional(self, ctx:KobraV2Parser.OpRelacionalContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Entero.
    def enterEntero(self, ctx:KobraV2Parser.EnteroContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Entero.
    def exitEntero(self, ctx:KobraV2Parser.EnteroContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#OpMultiplicativa.
    def enterOpMultiplicativa(self, ctx:KobraV2Parser.OpMultiplicativaContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#OpMultiplicativa.
    def exitOpMultiplicativa(self, ctx:KobraV2Parser.OpMultiplicativaContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Parentesis.
    def enterParentesis(self, ctx:KobraV2Parser.ParentesisContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Parentesis.
    def exitParentesis(self, ctx:KobraV2Parser.ParentesisContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#OpLogica.
    def enterOpLogica(self, ctx:KobraV2Parser.OpLogicaContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#OpLogica.
    def exitOpLogica(self, ctx:KobraV2Parser.OpLogicaContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Cadena.
    def enterCadena(self, ctx:KobraV2Parser.CadenaContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Cadena.
    def exitCadena(self, ctx:KobraV2Parser.CadenaContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#Booleano.
    def enterBooleano(self, ctx:KobraV2Parser.BooleanoContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#Booleano.
    def exitBooleano(self, ctx:KobraV2Parser.BooleanoContext):
        pass


    # Enter a parse tree produced by KobraV2Parser#OpAditiva.
    def enterOpAditiva(self, ctx:KobraV2Parser.OpAditivaContext):
        pass

    # Exit a parse tree produced by KobraV2Parser#OpAditiva.
    def exitOpAditiva(self, ctx:KobraV2Parser.OpAditivaContext):
        pass



del KobraV2Parser