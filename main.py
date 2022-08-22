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

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.button import Button
# Classes format:
# name : {name: name, attr: [attributes], methods: [methods]}
pp = pprint.PrettyPrinter(indent=4)


def check_types(left_side, right_side):
    return left_side.type == right_side.type


def check_for_errors(results):
    return [check_types(TreeReturn(one_result.type), TreeReturn("Error")) for one_result in results]


Attr = namedtuple("Attr", ["name", "type", "valid"])
Method = namedtuple("Method", ["name", "return_type", "args", "valid"])
Formal = namedtuple("Formal", ["name", "type"])
Feature = namedtuple("Feature", ["attributes", "methods", "valid"])
AttrInfo = namedtuple("AttrInfo", ["type", "valid"])
MethodInfo = namedtuple("MethodInfo", ["valid"])


class MyVisitor(MyGrammerVisitor):
    def check_symbol_table(self, symbol_name):
        return self.symbol_table.check_for_symbol(symbol_name)

    def check_inheritance(self, child, father):
        return self.type_table.does_inherit(child, father)

    def visitProgram(self, ctx):
        self.type_table = TypeTable()
        self.symbol_table = SymbolTable()
        # value = ctx.getText()
        # return int(value)
        features_returns = []
        for class_to_visit in ctx.classP():
            features_returns.append(sum(check_for_errors(self.visit(class_to_visit))))
        # self.visitChildren(ctx)
        print(f"Whole program has {sum(features_returns)} errors")
        # print('Classes')
        # pp.pprint(self.type_table.get_classes())
        # print('Methods')
        # pp.pprint(self.type_table.get_methods())
        # print('Attributes')
        # pp.pprint(self.type_table.get_attributes())
        # print('Arguments')
        # pp.pprint(self.type_table.get_arguments())
        # print('Symbol table')
        # pp.pprint(self.symbol_table.get_symbol_table())
        return "Return final"

    def visitClassP(self, ctx):
        self.symbol_table.add_scope()
        class_name = ctx.name.text
        result = self.visit(ctx.features())
        inherits = None
        if ctx.inheritName:
            inherits = ctx.inheritName.text
        self.type_table.add_type(class_name, result.attributes, result.methods, inheritance=inherits)
        self.symbol_table.remove_scope()
        return result.valid

    def visitFeatures(self, ctx):
        attributes = []
        methods = []
        validity = []
        for feature in ctx.feature():
            result = self.visit(feature)
            if type(result).__name__ == "Attr":
                attributes.append(result.name)
                validity.append(result.valid)
            if type(result).__name__ == "Method":
                methods.append(result.name)
                validity.append(result.valid)
        return Feature(attributes, methods, validity)

    def visitFeature(self, ctx):
        if ctx.featureAttr:
            type_name = self.visit(ctx.featureAttr)
            self.type_table.add_attribute(ctx.name.text, type_name.type)
            self.symbol_table.add_symbol(ctx.name.text, type_name.type)
            return Attr(ctx.name.text, type_name, type_name.valid)
        if ctx.featureMethod:
            method = self.visit(ctx.featureMethod)
            self.type_table.add_method(ctx.name.text, method[1], method[0])
            self.symbol_table.add_symbol(ctx.name.text, method[0])
            return Method(ctx.name.text, method[0], method[1], method[2])
        return

    def visitAttribute(self, ctx):
        if ctx.attrExpr:
            actual_type = self.visit(ctx.attrExpr)
            print(f"Actual_type {actual_type} declared_type {ctx.typeName.text}")
            print(f"Inherits {self.check_inheritance(ctx.typeName.text, actual_type.type)}")
            has_error = not check_types(actual_type, TreeReturn(ctx.typeName.text)) or actual_type.type == "Error"
            if has_error:
                print(f"ERROR in line {ctx.start.line} declared type {ctx.typeName.text} does not match with actual type {actual_type.type}")
            return AttrInfo(ctx.typeName.text, TreeReturn("Error") if has_error else TreeReturn("Valid"))
        return AttrInfo(ctx.typeName.text, TreeReturn("Valid"))

    def visitMethod(self, ctx):
        self.symbol_table.add_scope()
        arguments = self.visit(ctx.argumentList)
        has_error = self.visit(ctx.mainExpr)
        self.symbol_table.remove_scope()
        return ctx.returnType.text, arguments, has_error

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
        return_types = []
        for eachExpr in ctx.expr():
            return_types.append(self.visit(eachExpr))
        return TreeReturn("Error") if sum(check_for_errors(return_types)) else TreeReturn("Valid")

    # TODO Pensar retorno de multipleExpr
    def visitExpr(self, ctx):
        method_return = None
        if ctx.nextExpr:
            operations_result = self.visit(ctx.operations())
            has_method_call = operations_result[0]
            result = operations_result[1]
            if not has_method_call:
                if result.type == "Error":
                    print(f"ERROR in line {ctx.start.line} right side expected Int found {result.type}")
                    return TreeReturn("Error")
            else:
                method_return = result
        if ctx.stringE:
            return TreeReturn("String")
        if ctx.ifE:
            return self.visit(ctx.ifE)
        if ctx.whileE:
            return self.visit(ctx.whileE)
        if ctx.parenE:
            return self.visit(ctx.parenE)
        if ctx.innerExpr:
            return self.visit(ctx.innerExpr)
        if ctx.calls:
            return_type = self.visit(ctx.calls)
            if method_return:
                return method_return
            return return_type
        if ctx.let:
            return self.visit(ctx.let)
        if ctx.isVoid:
            return self.visit(ctx.isVoid)
        if ctx.notE:
            return self.visit(ctx.notE)
        if ctx.newDeclaration:
            return self.visit(ctx.newDeclaration)
        if ctx.boolE:
            return TreeReturn("Bool")
        if ctx.intE:
            return TreeReturn("Int")
        return TreeReturn("N/A")

    def visitNotEmpty(self, ctx):
        if ctx.rightSide:
            return True, self.visit(ctx.rightSide)
        if ctx.mCall:
            # print(f"MCall returned {self.visit(ctx.mCall)}")
            return True, self.visit(ctx.mCall)

    def visitMethodCall(self, ctx):
        if ctx.methodName.text not in self.type_table.get_methods():
            print("Error")
            return TreeReturn("Error")
        print(f"In MCall {ctx.methodName.text} {self.type_table.get_methods()[ctx.methodName.text]['return_type']}")
        return TreeReturn(self.type_table.get_methods()[ctx.methodName.text]['return_type'])

    def visitEscape(self, ctx):
        return False, TreeReturn("Escaped")

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIfExpr(self, ctx):
        condition_type = self.visit(ctx.cond)
        then_type = self.visit(ctx.thenExpr)
        else_type = self.visit(ctx.elseExpr)
        has_error = check_types(condition_type, TreeReturn("Error")) or check_types(then_type, TreeReturn("Error")) or check_types(else_type, TreeReturn("Error"))
        return TreeReturn("Error") if has_error else TreeReturn("Valid")

    def visitWhileExpr(self, ctx):
        condition_type = self.visit(ctx.cond)
        main_type = self.visit(ctx.mainExpr)
        has_error = check_types(condition_type, TreeReturn("Error")) or check_types(main_type, TreeReturn("Error"))
        return TreeReturn("Error") if has_error else TreeReturn("Valid")

    def visitNotExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIsVoidExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitOverwrite(self, ctx):
        if not self.check_symbol_table(ctx.name.text):
            print(f"ERROR in line {ctx.start.line} {ctx.name.text} not defined")
            return TreeReturn("Error")
        if ctx.attr:
            actual_type = self.visit(ctx.attr)
            symbol_table = self.symbol_table.find_symbol(ctx.name.text)
            if check_types(TreeReturn(symbol_table), actual_type):
                return TreeReturn("Valid")
            else:
                print(f"ERROR in line {ctx.start.line} declared type2 {symbol_table} does not match {actual_type}")
                return TreeReturn("Error")
        if ctx.fun:
            return_type = self.symbol_table.find_symbol(ctx.name.text)
            return TreeReturn(return_type)
        if not (ctx.attr or ctx.fun):
            return TreeReturn(self.symbol_table.find_symbol(ctx.name.text))
        return

    def visitLetExpr(self, ctx):
        self.symbol_table.add_scope()
        exprs = []
        for argExpr in ctx.initialExpr():
            exprs.append(self.visit(argExpr))
        # for i in exprs:
        #     print(i, ctx.start.line)
        result = self.visit(ctx.mainExpr)
        values = check_types(result, TreeReturn("Error"))
        self.symbol_table.remove_scope()
        return TreeReturn("Error") if values else TreeReturn("Valid")

    def visitDeclaration(self, ctx):
        if ctx.typeName.text not in self.type_table.get_classes():
            print(f"ERROR in line {ctx.start.line} {ctx.typeName.text} does not exist")
        return TreeReturn(ctx.typeName.text)

    def visitInitialExpr(self, ctx):
        self.symbol_table.add_symbol(ctx.name.text, ctx.typeName.text)
        # print('Symbol table')
        # pp.pprint(self.symbol_table.get_symbol_table())
        if ctx.actualExpr:
            actual_type = self.visit(ctx.actualExpr)
            has_error = not check_types(actual_type, TreeReturn(ctx.typeName.text)) or actual_type.type == "Error"
            return TreeReturn("Error") if has_error else TreeReturn("Valid")
        return TreeReturn("Valid")

    def visitAttrWrite(self, ctx):
        return_type = self.visit(ctx.attrInner)
        return return_type

class PongApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='horizontal')
        # LEFT LAYOUT
        self.left_layout = BoxLayout(orientation='vertical')
        self.left_input = TextInput(text="""
class Radio {
    currentStation:Int <- 123 + 321;
    getCurrent():Int{
        currentStation
    };
    changeStation(arg1:Int, arg2: Int):Int{
        {
            currentStation <- getCurrent();
            let letArg1: Int <- 123, letArg2: Int <- 2 in {
                letArg1 <- currentStation;
                letArg2 <- letArg2;
            };
        }
    };
};

class Toshiba INHERITS Radio {
    
};

class Car {
    myRadio: Toshiba <- new Radio;
    currentStation: Int;
    changeRadio(): Int{
        {
            currentStation <- myRadio.getCurrent();
            if currentStation = 60 then 61 else 59 fi;           
        }
    };
    getCurrentStation(): Int {
        currentStation
    };
};

class Main inherits IO {
    myCar: Car <- new Car;
    main() : SELF_TYPE {
        {
            out_string(myCar.getCurrentStation());
        }
    };
};
""", multiline=True)
        self.left_layout.add_widget(self.left_input)

        # MIDDLE LAYOUT
        self.middle_layout = BoxLayout(orientation='vertical', spacing=10)
        self.middle_label = Label(text="Middle", font_size=30, size_hint=(1, 0.1))
        self.check_type_button = Button(text="Check types", size_hint=(1, 0.3), on_press=self.update)
        self.middle_layout.add_widget(self.middle_label)
        self.middle_layout.add_widget(self.check_type_button)

        # RIGHT LAYOUT
        self.right_layout = BoxLayout(orientation='vertical')
        self.tabbed = TabbedPanel(do_default_tab=False)
        self.tabbed_header = TabbedPanelHeader(text="Tab1")
        self.right_output = Label(text="Output", font_size=12)
        self.tabbed_header.content = self.right_output
        self.tabbed.add_widget(self.tabbed_header)
        self.right_layout.add_widget(self.tabbed)

        # MAIN LAYOUT ASSEMBLY
        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.middle_layout)
        self.main_layout.add_widget(self.right_layout)
        return self.main_layout

    def update(self, event):
        self.right_output.text = self.left_input.text
        self.make_magic()

    def make_magic(self):
        data_to_check = InputStream(self.left_input.text)
        # lexer
        lexer = MyGrammerLexer(data_to_check)
        stream = CommonTokenStream(lexer)
        # parser
        parser = MyGrammerParser(stream)
        tree = parser.program()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(F"OUTPUT{output}")

if __name__ == "__main__":
    while 1:
        data =  InputStream("""
class Radio {
    currentStation:Int <- 123 + 321;
    resetStation():Int{
        5
    };
    changeStation(arg1:Int, arg2: Int):Int{
        {
            currentStation <- resetStation();
            let letArg1: Int <- 123, letArg2: Int <- 2 in {
                letArg1 <- currentStation;
                letArg2 <- letArg2;
            };
        }
    };
};

class Car {
    myRadio: Radio <- new Radio;
};
""")
        break
    PongApp().run()
