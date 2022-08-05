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
# Classes format:
# name : {name: name, attr: [attributes], methods: [methods]}
pp = pprint.PrettyPrinter(indent=4)
class MyVisitor(MyGrammerVisitor):

    def check_types(self, left_side, right_side):
        return left_side.type == right_side.type

    def visitProgram(self, ctx):
        self.type_table = TypeTable()
        self.symbol_table = SymbolTable()
        self.symbol_methods = {}
        self.symbol_attributes = {}
        self.symbol_arguments = {}
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
        self.current_class = ctx.name.text
        self.current_methods = []
        self.current_attributes = []
        # return self.visit(ctx.expr())
        self.visitChildren(ctx)
        self.type_table.add_type(self.current_class, self.current_attributes, self.current_methods)
        self.symbol_table.remove_scope()
        return ctx.getText()

    def visitFeature(self, ctx):
        self.current_feature = ctx.name.text
        self.visitChildren(ctx)
        return ctx.name.text

    # Method format:
    # name : {name : name, args: {name: {'name': name, 'type':type}}, type: type}
    def visitMethod(self, ctx):
        self.symbol_table.add_symbol(self.current_feature, ctx.returnType.text)
        self.symbol_table.add_scope()
        self.current_methods.append(self.current_feature)
        self.current_arguments = []
        self.visit(ctx.argumentList)
        self.visit(ctx.mainExpr)
        self.type_table.add_method(self.current_feature, self.current_arguments, ctx.returnType.text)
        self.symbol_table.remove_scope()
        return

    def visitArguments(self, ctx):
        self.visitChildren(ctx)
        return

    # Attribute format:
    # name : {name : name, type: type}
    def visitAttribute(self, ctx):
        type_name = ctx.typeName.text
        declared_type = TreeReturn(type_name)
        actual_type = TreeReturn(self.visit(ctx.attrExpr))
        if self.type_table.type_exists(type_name):
            pass
        else:
            print("Not found attribute")
        self.symbol_table.add_symbol(self.current_feature, type_name)
        self.type_table.add_attribute(self.current_feature, type_name)
        self.current_attributes.append(self.current_feature)
        return declared_type if self.check_types(declared_type, actual_type) else TreeReturn("Error")

    def visitFormal(self, ctx):
        self.type_table.add_argument(ctx.name.text, ctx.typeName.text)
        self.symbol_table.add_symbol(ctx.name.text, ctx.typeName.text)
        self.current_arguments.append(ctx.name.text)
        return

    def visitExpr(self, ctx):
        to_return = TreeReturn("Error")
        if ctx.calls:
            self.visit(ctx.calls)
        if ctx.innerExpr:
            self.visit(ctx.innerExpr)
        if ctx.let:
            self.symbol_table.add_scope()
            self.visit(ctx.let)
            print('Let', self.symbol_table.peek())
            self.symbol_table.remove_scope()
        if ctx.newDeclaration:
            to_return = TreeReturn(self.visit(ctx.newDeclaration))
        if ctx.intE:
            to_return = TreeReturn("Int")
        if ctx.stringE:
            to_return = TreeReturn("String")
        if ctx.falseE or ctx.trueE:
            to_return = TreeReturn("Bool")
        self.visit(ctx.nextExpr)
        return to_return

    def visitDeclaration(self, ctx):
        return ctx.typeName.text

    def visitMultipleExpr(self, ctx):
        self.visitChildren(ctx)
        return

    def visitLetExpr(self, ctx):
        print("My Expr")
        pp.pprint(self.symbol_table.get_symbol_table())
        self.visit(ctx.initial)
        return

    def visitInitialExpr(self, ctx):
        name = ctx.name.text
        type_name = ctx.typeName.text
        if self.type_table.type_exists(type_name):
            pass
        else:
            print("Not found initialExpr")
        return

    def visitFollowingExpr(self, ctx):
        return

    def visitExpr2(self, ctx):
        if ctx.mCall:
            self.visit(ctx.mCall)
        # self.visitChildren(ctx)
        return

    def visitMethodCall(self, ctx):
        print('Checking call', ctx.methodName.text)
        return

    def visitOverwrite(self, ctx):
        return_type = None
        ### Check current_overwrite problem
        self.current_overwrite = ctx.name.text
        print(f"Current overwrite {self.current_overwrite}")
        if ctx.attr:
            return_type = TreeReturn(self.visit(ctx.attr))
        if ctx.fun:
            return_type = TreeReturn(self.visit(ctx.fun))
        if not (ctx.attr or ctx.fun):
            return_type = TreeReturn(self.symbol_table.find_symbol(self.current_overwrite))
        if self.symbol_table.check_for_symbol(ctx.name.text):
            # print('Found', ctx.name.text)
            pass
        else:
            pp.pprint(self.symbol_table.get_symbol_table())
            print(f"Not found overwrite {ctx.name.text}")
        return return_type

    # Visit a parse tree produced by MyGrammerParser#attrWrite.
    def visitAttrWrite(self, ctx):
        # self.visitChildren(ctx)
        type_name = TreeReturn(self.symbol_table.find_symbol(self.current_overwrite))
        actual_type = TreeReturn(self.visit(ctx.attrInner))
        print(f"Checked types for {self.current_overwrite} {type_name} {actual_type}")
        return self.visit(ctx.attrInner)


    # Visit a parse tree produced by MyGrammerParser#funCall.
    def visitFunCall(self, ctx):
        return self.visitChildren(ctx)


if __name__ == "__main__":
    while 1:
        data =  InputStream("""
class Radio {
    isOn:Bool <- false;
    currentStation:Int <- 123;
    turn_on():Bool{
        isOn <- true
    };
    turn_off():Bool{
        isOn <- false
    };
    change_station(newStation : Int, som : Int): Int{
        currentStation <- newStation + som
    };
};

class Main {
 myRadio:Radio <- new Radio;
 main(): SELF_TYPE {
        {
            myRadio.turnOn();
            myRadio.change(5);
            myRadio.turnOff();
            let inner1: Int <- 1, inner2:Int <- 5 in {
                inner1 <- inner1 + inner2;
            };
        }
    };
};""")
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
