import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
import pprint
from tkinter import *
from tkinter import ttk
from TypeTable import TypeTable
from SymbolTable import SymbolTable
from TreeReturn import TreeReturn
from collections import namedtuple
# Classes format:
# name : {name: name, attr: [attributes], methods: [methods]}
pp = pprint.PrettyPrinter(indent=4)


def check_types(left_side, right_side):
    return left_side.type == right_side.type


Attr = namedtuple("Attr", ["name", "type"])
Method = namedtuple("Method", ["name", "return_type", "args"])
Formal = namedtuple("Formal", ["name", "type"])
Feature = namedtuple("Feature", ["attributes", "methods"])

class MyVisitor(MyGrammerVisitor):

    def visitProgram(self, ctx):
        self.type_table = TypeTable()
        self.symbol_table = SymbolTable()
        # value = ctx.getText()
        # return int(value)
        self.visitChildren(ctx)
        print('Classes')
        pp.pprint(self.type_table.get_classes())
        print('Methods')
        pp.pprint(self.type_table.get_methods())
        print('Attributes')
        pp.pprint(self.type_table.get_attributes())
        print('Arguments')
        pp.pprint(self.type_table.get_arguments())
        print('Symbol table')
        pp.pprint(self.symbol_table.get_symbol_table())
        return

    def visitClassP(self, ctx):
        self.symbol_table.add_scope()
        class_name = ctx.name.text
        result = self.visit(ctx.features())
        self.type_table.add_type(class_name, result.attributes, result.methods)
        self.symbol_table.remove_scope()
        return ctx.getText()

    def visitFeatures(self, ctx):
        attributes = []
        methods = []
        for feature in ctx.feature():
            result = self.visit(feature)
            if type(result).__name__ == "Attr":
                attributes.append(result.name)
            if type(result).__name__ == "Method":
                methods.append(result.name)
        return Feature(attributes, methods)

    def visitFeature(self, ctx):
        if ctx.featureAttr:
            type_name = self.visit(ctx.featureAttr)
            self.type_table.add_attribute(ctx.name.text, type_name)
            self.symbol_table.add_symbol(ctx.name.text, type_name)
            return Attr(ctx.name.text, type_name)
        if ctx.featureMethod:
            method = self.visit(ctx.featureMethod)
            self.type_table.add_method(ctx.name.text, method[1], method[0])
            self.symbol_table.add_symbol(ctx.name.text, method[0])
            return Method(ctx.name.text, method[0], method[1])
        return

    def visitAttribute(self, ctx):
        return ctx.typeName.text

    def visitMethod(self, ctx):
        self.symbol_table.add_scope()
        arguments = self.visit(ctx.argumentList)
        self.visit(ctx.mainExpr)
        self.symbol_table.remove_scope()
        return ctx.returnType.text, arguments

    def visitArguments(self, ctx):
        arguments = []
        for arg in ctx.formal():
            returned_arguments = self.visit(arg)
            arguments.append(returned_arguments.name)
            self.symbol_table.add_symbol(returned_arguments.name, returned_arguments.type)
        return arguments

    def visitFormal(self, ctx):
        self.type_table.add_argument(ctx.name.text, ctx.typeName.text)
        return Formal(ctx.name.text, ctx.typeName.text)

    def visitMultipleExpr(self, ctx):
        for eachExpr in ctx.expr():
            self.visit(eachExpr)
        return

    def visitExpr(self, ctx):
        if ctx.innerExpr:
            self.visit(ctx.innerExpr)
        if ctx.let:
            self.visit(ctx.let)
        return

    # TODO Add let exprs to symbol table
    def visitLetExpr(self, ctx):
        self.symbol_table.add_scope()
        print("Current table")
        for argExpr in ctx.initialExpr():
            self.visit(argExpr)
        pp.pprint(self.symbol_table.get_symbol_table())
        self.symbol_table.remove_scope()
        return

    def visitInitialExpr(self, ctx):
        self.symbol_table.add_symbol(ctx.name.text, ctx.typeName.text)
        return

if __name__ == "__main__":
    while 1:
        data =  InputStream("""
class Radio {
    currentStation:Int <- 123;
    changeStation(arg1:Int, arg2: Int):Int{
        {
            currentStation <- 321;
            let letArg1: Int <- 1, letArg2: Int <- 2 in {
                {
                    letArg1 <- currentStation + 5;
                };
            };
        }
    };
};

class Car {
    myRadio: Radio <- new Radio;
};
""")
        # lexer
        lexer = MyGrammerLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = MyGrammerParser(stream)
        tree = parser.program()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        # print(Trees.toStringTree(tree, None, parser))
        break
