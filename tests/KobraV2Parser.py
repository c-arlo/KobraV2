# Generated from src/KobraV2.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,
        1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,55,8,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,77,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,112,8,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,129,8,11,10,11,12,11,132,9,11,1,11,0,1,22,12,0,2,4,6,8,
        10,12,14,16,18,20,22,0,5,1,0,24,25,1,0,7,8,1,0,9,12,1,0,13,14,1,
        0,15,16,141,0,27,1,0,0,0,2,39,1,0,0,0,4,41,1,0,0,0,6,50,1,0,0,0,
        8,58,1,0,0,0,10,63,1,0,0,0,12,69,1,0,0,0,14,78,1,0,0,0,16,84,1,0,
        0,0,18,94,1,0,0,0,20,98,1,0,0,0,22,111,1,0,0,0,24,26,3,2,1,0,25,
        24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,
        0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,40,3,6,3,0,33,40,3,
        8,4,0,34,40,3,10,5,0,35,40,3,12,6,0,36,40,3,14,7,0,37,40,3,16,8,
        0,38,40,3,20,10,0,39,32,1,0,0,0,39,33,1,0,0,0,39,34,1,0,0,0,39,35,
        1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,
        45,5,1,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,
        0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,2,0,0,49,5,1,
        0,0,0,50,51,5,17,0,0,51,54,5,26,0,0,52,53,5,3,0,0,53,55,3,22,11,
        0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,5,4,0,0,57,7,1,
        0,0,0,58,59,5,26,0,0,59,60,5,3,0,0,60,61,3,22,11,0,61,62,5,4,0,0,
        62,9,1,0,0,0,63,64,5,23,0,0,64,65,5,5,0,0,65,66,3,22,11,0,66,67,
        5,6,0,0,67,68,5,4,0,0,68,11,1,0,0,0,69,70,5,19,0,0,70,71,5,5,0,0,
        71,72,3,22,11,0,72,73,5,6,0,0,73,76,3,4,2,0,74,75,5,20,0,0,75,77,
        3,4,2,0,76,74,1,0,0,0,76,77,1,0,0,0,77,13,1,0,0,0,78,79,5,21,0,0,
        79,80,5,5,0,0,80,81,3,22,11,0,81,82,5,6,0,0,82,83,3,4,2,0,83,15,
        1,0,0,0,84,85,5,22,0,0,85,86,5,5,0,0,86,87,3,18,9,0,87,88,5,4,0,
        0,88,89,3,22,11,0,89,90,5,4,0,0,90,91,3,18,9,0,91,92,5,6,0,0,92,
        93,3,4,2,0,93,17,1,0,0,0,94,95,5,26,0,0,95,96,5,3,0,0,96,97,3,22,
        11,0,97,19,1,0,0,0,98,99,3,22,11,0,99,100,5,4,0,0,100,21,1,0,0,0,
        101,102,6,11,-1,0,102,103,5,5,0,0,103,104,3,22,11,0,104,105,5,6,
        0,0,105,112,1,0,0,0,106,112,5,26,0,0,107,112,5,27,0,0,108,112,5,
        28,0,0,109,112,5,29,0,0,110,112,5,18,0,0,111,101,1,0,0,0,111,106,
        1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,110,
        1,0,0,0,112,130,1,0,0,0,113,114,10,11,0,0,114,115,7,0,0,0,115,129,
        3,22,11,12,116,117,10,10,0,0,117,118,7,1,0,0,118,129,3,22,11,11,
        119,120,10,9,0,0,120,121,7,2,0,0,121,129,3,22,11,10,122,123,10,8,
        0,0,123,124,7,3,0,0,124,129,3,22,11,9,125,126,10,7,0,0,126,127,7,
        4,0,0,127,129,3,22,11,8,128,113,1,0,0,0,128,116,1,0,0,0,128,119,
        1,0,0,0,128,122,1,0,0,0,128,125,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,23,1,0,0,0,132,130,1,0,0,0,8,27,39,45,
        54,76,111,128,130
    ]

class KobraV2Parser ( Parser ):

    grammarFileName = "KobraV2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "';'", "'('", "')'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", "'SI'", 
                     "'SINO'", "'MIENTRAS'", "'PARA'", "'IMPRIMIR'", "'Y'", 
                     "'O'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TIPO", "BOOL_LIT", "SI", "SINO", "MIENTRAS", 
                      "PARA", "IMPRIMIR", "Y", "O", "ID", "INT", "FLOAT", 
                      "STRING", "COMENTARIO", "WS" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_bloque = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_impresion = 5
    RULE_si_stmt = 6
    RULE_while_stmt = 7
    RULE_for_stmt = 8
    RULE_asignacion_for = 9
    RULE_expresion_stmt = 10
    RULE_expresion = 11

    ruleNames =  [ "programa", "instruccion", "bloque", "declaracion", "asignacion", 
                   "impresion", "si_stmt", "while_stmt", "for_stmt", "asignacion_for", 
                   "expresion_stmt", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    TIPO=17
    BOOL_LIT=18
    SI=19
    SINO=20
    MIENTRAS=21
    PARA=22
    IMPRIMIR=23
    Y=24
    O=25
    ID=26
    INT=27
    FLOAT=28
    STRING=29
    COMENTARIO=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KobraV2Parser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = KobraV2Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1022230560) != 0):
                self.state = 24
                self.instruccion()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(KobraV2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(KobraV2Parser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(KobraV2Parser.AsignacionContext,0)


        def impresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ImpresionContext,0)


        def si_stmt(self):
            return self.getTypedRuleContext(KobraV2Parser.Si_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(KobraV2Parser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(KobraV2Parser.For_stmtContext,0)


        def expresion_stmt(self):
            return self.getTypedRuleContext(KobraV2Parser.Expresion_stmtContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = KobraV2Parser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.impresion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.si_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 38
                self.expresion_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = KobraV2Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(KobraV2Parser.T__0)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1022230560) != 0):
                self.state = 42
                self.instruccion()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(KobraV2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(KobraV2Parser.TIPO, 0)

        def ID(self):
            return self.getToken(KobraV2Parser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = KobraV2Parser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(KobraV2Parser.TIPO)
            self.state = 51
            self.match(KobraV2Parser.ID)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 52
                self.match(KobraV2Parser.T__2)
                self.state = 53
                self.expresion(0)


            self.state = 56
            self.match(KobraV2Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KobraV2Parser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = KobraV2Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(KobraV2Parser.ID)
            self.state = 59
            self.match(KobraV2Parser.T__2)
            self.state = 60
            self.expresion(0)
            self.state = 61
            self.match(KobraV2Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(KobraV2Parser.IMPRIMIR, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = KobraV2Parser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(KobraV2Parser.IMPRIMIR)
            self.state = 64
            self.match(KobraV2Parser.T__4)
            self.state = 65
            self.expresion(0)
            self.state = 66
            self.match(KobraV2Parser.T__5)
            self.state = 67
            self.match(KobraV2Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Si_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(KobraV2Parser.SI, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.BloqueContext,i)


        def SINO(self):
            return self.getToken(KobraV2Parser.SINO, 0)

        def getRuleIndex(self):
            return KobraV2Parser.RULE_si_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi_stmt" ):
                listener.enterSi_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi_stmt" ):
                listener.exitSi_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi_stmt" ):
                return visitor.visitSi_stmt(self)
            else:
                return visitor.visitChildren(self)




    def si_stmt(self):

        localctx = KobraV2Parser.Si_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_si_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(KobraV2Parser.SI)
            self.state = 70
            self.match(KobraV2Parser.T__4)
            self.state = 71
            self.expresion(0)
            self.state = 72
            self.match(KobraV2Parser.T__5)
            self.state = 73
            self.bloque()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 74
                self.match(KobraV2Parser.SINO)
                self.state = 75
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(KobraV2Parser.MIENTRAS, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(KobraV2Parser.BloqueContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = KobraV2Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(KobraV2Parser.MIENTRAS)
            self.state = 79
            self.match(KobraV2Parser.T__4)
            self.state = 80
            self.expresion(0)
            self.state = 81
            self.match(KobraV2Parser.T__5)
            self.state = 82
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(KobraV2Parser.PARA, 0)

        def asignacion_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.Asignacion_forContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.Asignacion_forContext,i)


        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(KobraV2Parser.BloqueContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = KobraV2Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(KobraV2Parser.PARA)
            self.state = 85
            self.match(KobraV2Parser.T__4)
            self.state = 86
            self.asignacion_for()
            self.state = 87
            self.match(KobraV2Parser.T__3)
            self.state = 88
            self.expresion(0)
            self.state = 89
            self.match(KobraV2Parser.T__3)
            self.state = 90
            self.asignacion_for()
            self.state = 91
            self.match(KobraV2Parser.T__5)
            self.state = 92
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KobraV2Parser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_asignacion_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_for" ):
                listener.enterAsignacion_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_for" ):
                listener.exitAsignacion_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion_for" ):
                return visitor.visitAsignacion_for(self)
            else:
                return visitor.visitChildren(self)




    def asignacion_for(self):

        localctx = KobraV2Parser.Asignacion_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_asignacion_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(KobraV2Parser.ID)
            self.state = 95
            self.match(KobraV2Parser.T__2)
            self.state = 96
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraV2Parser.RULE_expresion_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_stmt" ):
                listener.enterExpresion_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_stmt" ):
                listener.exitExpresion_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion_stmt" ):
                return visitor.visitExpresion_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expresion_stmt(self):

        localctx = KobraV2Parser.Expresion_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expresion_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.expresion(0)
            self.state = 99
            self.match(KobraV2Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KobraV2Parser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(KobraV2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class FlotanteContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(KobraV2Parser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlotante" ):
                listener.enterFlotante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlotante" ):
                listener.exitFlotante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlotante" ):
                return visitor.visitFlotante(self)
            else:
                return visitor.visitChildren(self)


    class OpIgualdadContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpIgualdad" ):
                listener.enterOpIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpIgualdad" ):
                listener.exitOpIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpIgualdad" ):
                return visitor.visitOpIgualdad(self)
            else:
                return visitor.visitChildren(self)


    class OpRelacionalContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpRelacional" ):
                listener.enterOpRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpRelacional" ):
                listener.exitOpRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpRelacional" ):
                return visitor.visitOpRelacional(self)
            else:
                return visitor.visitChildren(self)


    class EnteroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(KobraV2Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntero" ):
                listener.enterEntero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntero" ):
                listener.exitEntero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntero" ):
                return visitor.visitEntero(self)
            else:
                return visitor.visitChildren(self)


    class OpMultiplicativaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMultiplicativa" ):
                listener.enterOpMultiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMultiplicativa" ):
                listener.exitOpMultiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMultiplicativa" ):
                return visitor.visitOpMultiplicativa(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class OpLogicaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,i)

        def Y(self):
            return self.getToken(KobraV2Parser.Y, 0)
        def O(self):
            return self.getToken(KobraV2Parser.O, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpLogica" ):
                listener.enterOpLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpLogica" ):
                listener.exitOpLogica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLogica" ):
                return visitor.visitOpLogica(self)
            else:
                return visitor.visitChildren(self)


    class CadenaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(KobraV2Parser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCadena" ):
                listener.enterCadena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCadena" ):
                listener.exitCadena(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCadena" ):
                return visitor.visitCadena(self)
            else:
                return visitor.visitChildren(self)


    class BooleanoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LIT(self):
            return self.getToken(KobraV2Parser.BOOL_LIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleano" ):
                listener.enterBooleano(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleano" ):
                listener.exitBooleano(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleano" ):
                return visitor.visitBooleano(self)
            else:
                return visitor.visitChildren(self)


    class OpAditivaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KobraV2Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraV2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraV2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAditiva" ):
                listener.enterOpAditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAditiva" ):
                listener.exitOpAditiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAditiva" ):
                return visitor.visitOpAditiva(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KobraV2Parser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = KobraV2Parser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self.match(KobraV2Parser.T__4)
                self.state = 103
                self.expresion(0)
                self.state = 104
                self.match(KobraV2Parser.T__5)
                pass
            elif token in [26]:
                localctx = KobraV2Parser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(KobraV2Parser.ID)
                pass
            elif token in [27]:
                localctx = KobraV2Parser.EnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(KobraV2Parser.INT)
                pass
            elif token in [28]:
                localctx = KobraV2Parser.FlotanteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(KobraV2Parser.FLOAT)
                pass
            elif token in [29]:
                localctx = KobraV2Parser.CadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(KobraV2Parser.STRING)
                pass
            elif token in [18]:
                localctx = KobraV2Parser.BooleanoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(KobraV2Parser.BOOL_LIT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 128
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = KobraV2Parser.OpLogicaContext(self, KobraV2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 113
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expresion(12)
                        pass

                    elif la_ == 2:
                        localctx = KobraV2Parser.OpIgualdadContext(self, KobraV2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 116
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expresion(11)
                        pass

                    elif la_ == 3:
                        localctx = KobraV2Parser.OpRelacionalContext(self, KobraV2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 119
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expresion(10)
                        pass

                    elif la_ == 4:
                        localctx = KobraV2Parser.OpAditivaContext(self, KobraV2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 122
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expresion(9)
                        pass

                    elif la_ == 5:
                        localctx = KobraV2Parser.OpMultiplicativaContext(self, KobraV2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 125
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expresion(8)
                        pass

             
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




