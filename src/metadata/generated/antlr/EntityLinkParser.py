# Generated from /home/runner/work/OpenMetadata/OpenMetadata/openmetadata-spec/src/main/antlr4/org/openmetadata/schema/EntityLink.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\27\4\2\t\2\4\3\t\3\3\2\3\2\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\25\n\3\3\3\2\2\4\2\4")
        buf.write("\2\2\2\30\2\6\3\2\2\2\4\24\3\2\2\2\6\t\7\3\2\2\7\b\7\7")
        buf.write("\2\2\b\n\5\4\3\2\t\7\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2")
        buf.write("\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\4\2\2\16\17\7\2\2\3\17")
        buf.write("\3\3\2\2\2\20\25\7\5\2\2\21\25\7\b\2\2\22\25\7\t\2\2\23")
        buf.write("\25\7\6\2\2\24\20\3\2\2\2\24\21\3\2\2\2\24\22\3\2\2\2")
        buf.write("\24\23\3\2\2\2\25\5\3\2\2\2\4\13\24")
        return buf.getvalue()


class EntityLinkParser ( Parser ):

    grammarFileName = "EntityLink.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<#E'", "'>'", "<INVALID>", "<INVALID>", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ENTITY_TYPE", 
                      "ENTITY_FIELD", "RESERVED", "ENTITY_ATTRIBUTE", "ENTITY_FQN" ]

    RULE_entitylink = 0
    RULE_entity = 1

    ruleNames =  [ "entitylink", "entity" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ENTITY_TYPE=3
    ENTITY_FIELD=4
    RESERVED=5
    ENTITY_ATTRIBUTE=6
    ENTITY_FQN=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EntitylinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EntityLinkParser.EOF, 0)

        def RESERVED(self, i:int=None):
            if i is None:
                return self.getTokens(EntityLinkParser.RESERVED)
            else:
                return self.getToken(EntityLinkParser.RESERVED, i)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EntityLinkParser.EntityContext)
            else:
                return self.getTypedRuleContext(EntityLinkParser.EntityContext,i)


        def getRuleIndex(self):
            return EntityLinkParser.RULE_entitylink

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitylink" ):
                listener.enterEntitylink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitylink" ):
                listener.exitEntitylink(self)




    def entitylink(self):

        localctx = EntityLinkParser.EntitylinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entitylink)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(EntityLinkParser.T__0)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 5
                self.match(EntityLinkParser.RESERVED)
                self.state = 6
                self.entity()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EntityLinkParser.RESERVED):
                    break

            self.state = 11
            self.match(EntityLinkParser.T__1)
            self.state = 12
            self.match(EntityLinkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EntityLinkParser.RULE_entity

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EntityAttributeContext(EntityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EntityLinkParser.EntityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTITY_ATTRIBUTE(self):
            return self.getToken(EntityLinkParser.ENTITY_ATTRIBUTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityAttribute" ):
                listener.enterEntityAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityAttribute" ):
                listener.exitEntityAttribute(self)


    class EntityTypeContext(EntityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EntityLinkParser.EntityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTITY_TYPE(self):
            return self.getToken(EntityLinkParser.ENTITY_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityType" ):
                listener.enterEntityType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityType" ):
                listener.exitEntityType(self)


    class EntityFieldContext(EntityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EntityLinkParser.EntityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTITY_FIELD(self):
            return self.getToken(EntityLinkParser.ENTITY_FIELD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityField" ):
                listener.enterEntityField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityField" ):
                listener.exitEntityField(self)


    class EntityFqnContext(EntityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EntityLinkParser.EntityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTITY_FQN(self):
            return self.getToken(EntityLinkParser.ENTITY_FQN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityFqn" ):
                listener.enterEntityFqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityFqn" ):
                listener.exitEntityFqn(self)



    def entity(self):

        localctx = EntityLinkParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entity)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EntityLinkParser.ENTITY_TYPE]:
                localctx = EntityLinkParser.EntityTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(EntityLinkParser.ENTITY_TYPE)
                pass
            elif token in [EntityLinkParser.ENTITY_ATTRIBUTE]:
                localctx = EntityLinkParser.EntityAttributeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(EntityLinkParser.ENTITY_ATTRIBUTE)
                pass
            elif token in [EntityLinkParser.ENTITY_FQN]:
                localctx = EntityLinkParser.EntityFqnContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(EntityLinkParser.ENTITY_FQN)
                pass
            elif token in [EntityLinkParser.ENTITY_FIELD]:
                localctx = EntityLinkParser.EntityFieldContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(EntityLinkParser.ENTITY_FIELD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





