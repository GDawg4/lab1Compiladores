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
import numpy as np

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


Attr = namedtuple("Attr", ["name", "type", "valid", "size"], defaults=("Attr", "Object", True, 0))
Method = namedtuple("Method", ["name", "return_type", "args", "valid"])
Formal = namedtuple("Formal", ["name", "type"])
Feature = namedtuple("Feature", ["attributes", "methods", "valid", "size"])
AttrInfo = namedtuple("AttrInfo", ["type", "valid", "size"], defaults=("Valid", True, 0))
MethodInfo = namedtuple("MethodInfo", ["valid"])

# TODO: Revisar si m_todos ya existen con herencia, validar tipos en if y while
class MyVisitor(MyGrammerVisitor):
    def check_symbol_table(self, symbol_name):
        return self.symbol_table.check_for_symbol(symbol_name)

    def check_inheritance(self, child, father):
        return self.type_table.does_inherit(child, father)

    def visitProgram(self, ctx):
        self.current_number = 0
        self.current_if = 0
        self.current_while = 0
        self.quadruples = {}
        self.type_table = TypeTable()
        self.symbol_table = SymbolTable()
        # value = ctx.getText()
        # return int(value)
        features_returns = []
        self.has_main = False
        for class_to_visit in ctx.classP():
            features_returns.append(sum(check_for_errors(self.visit(class_to_visit))))
        if not self.has_main:
            print(f"ERROR in program, main does not exist")
        # self.visitChildren(ctx)
        # print(f"Whole program has {sum(features_returns)} errors")
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
        print('Intermediate code')
        pp.pprint(self.quadruples)
        for key, value in self.quadruples.items():
            if value['arg2'] is None:
                print(f"{value['result']} {value['op']} {value['arg1']}")
            else:
                print(f"{value['result']} {value['arg1']} {value['op']} {value['arg2']}")
        return "Return final"

    def get_new_label(self):
        new_label = f"label{self.current_number}"
        self.current_number += 1
        return new_label

    def get_new_if(self):
        new_if = f"label_if{self.current_if}"
        self.current_if += 1
        return new_if

    def get_new_while(self):
        new_while = f"label_while{self.current_while}"
        self.current_while += 1
        return new_while

    def visitClassP(self, ctx):
        self.symbol_table.add_scope()
        class_name = ctx.name.text
        if ctx.name.text == "main" or ctx.name.text == "Main":
            self.has_main = True
        self.current_class = class_name
        inherits = None
        self.inherits_from = None
        exists = False
        if ctx.inheritName:
            exists = self.type_table.type_exists(ctx.inheritName.text)
        if ctx.inheritName and exists:
            inherits = ctx.inheritName.text
            self.inherits_from = ctx.inheritName.text
        if ctx.inheritName and not exists:
            print(f"ERROR in line {ctx.start.line} class inherited does not exist")
        result = self.visit(ctx.features())
        self.type_table.add_type(class_name, result.attributes, result.methods, inheritance=inherits, size=result.size)
        self.symbol_table.remove_scope()
        return result.valid

    def visitFeatures(self, ctx):
        attributes = []
        methods = []
        validity = []
        total_size = 0
        for feature in ctx.feature():
            result = self.visit(feature)
            if type(result).__name__ == "Attr":
                attributes.append(result.name)
                validity.append(result.valid)
                total_size += result.size
            if type(result).__name__ == "Method":
                methods.append(result.name)
                validity.append(result.valid)
        return Feature(attributes, methods, validity, total_size)

    def visitFeature(self, ctx):
        already_exists = self.symbol_table.check_for_symbol(ctx.name.text)
        if ctx.featureAttr:
            type_name = self.visit(ctx.featureAttr)
            if already_exists:
                print(f"ERROR in line {ctx.start.line} attribute {ctx.name.text} already declared")
            else:
                self.type_table.add_attribute(ctx.name.text, type_name.type)
                self.symbol_table.add_symbol(ctx.name.text, type_name.type, size=self.type_table.get_size(type_name.type))
                print(f"{type_name.valid.code}")
                print(f"B[{self.symbol_table.get_pointer(ctx.name.text)}] = {type_name.valid.addr}")
                # print(f"{self.get_new_label()} = {actual_type.addr}")
                # print(f"Attr returned {type_name.valid}")
                return Attr(ctx.name.text, type_name, type_name.valid, type_name.size)
        if ctx.featureMethod:
            self.current_method_name = ctx.name.text
            method = self.visit(ctx.featureMethod)
            self.type_table.add_method(ctx.name.text, method[1], method[0])
            exists_in_parent = self.type_table.exists_in_parent(self.inherits_from, ctx.name.text)
            if exists_in_parent:
                old_arguments = self.type_table.get_methods()[ctx.name.text]['arguments']
                old_return = self.type_table.get_methods()[ctx.name.text]['return_type']
                has_same_signature = old_return == method[0] and old_arguments == method[1]
                if not has_same_signature:
                    print(F"ERROR in line {ctx.start.line} method {ctx.start.line} already declared with different signature")
            if already_exists:
                print(f"ERROR in line {ctx.start.line} method {ctx.name.text} already declared")
            else:
                print(f"\n{ctx.name.text}:{method[2].code}\n")
                type_to_check = method[0]
                # if method[0] == "SELF_TYPE":
                    # type_to_check = self.current_class
                if type_to_check != method[2].type:
                    print(f"ERROR in line {ctx.start.line} method {ctx.name.text} declared {method[0]} does not match {method[2].type}")
                return Method(ctx.name.text, method[0], method[1], method[2])
        return

    def add_quadruple(self, operator, arg1, arg2, result):
        self.quadruples[f't{self.current_number}'] = {
            'op': operator,
            'arg1': arg1,
            'arg2': arg2,
            'result': result
        }

    def visitAttribute(self, ctx):
        if ctx.attrExpr:
            actual_type = self.visit(ctx.attrExpr)
            self.current_number += 1
            has_error = not (check_types(actual_type, TreeReturn(ctx.typeName.text)) or self.check_inheritance(ctx.typeName.text, actual_type.type)) or actual_type.type == "Error"
            if has_error:
                print(f"ERROR in line {ctx.start.line} declared type {ctx.typeName.text} does not match with actual type {actual_type.type}")
            return AttrInfo(ctx.typeName.text, TreeReturn("Error") if has_error else TreeReturn("Valid", addr=actual_type.addr, code=actual_type.code), self.type_table.get_size(ctx.typeName.text))
        return AttrInfo(ctx.typeName.text, TreeReturn("Valid"), self.type_table.get_size(ctx.typeName.text))

    def visitMethod(self, ctx):
        # self.symbol_table.add_scope()
        # print("BEFORE")
        # pp.pprint(self.symbol_table.get_symbol_table())
        arguments = self.visit(ctx.argumentList)
        self.symbol_table.add_symbol(self.current_method_name, ctx.returnType.text, arguments)
        has_error = self.visit(ctx.mainExpr)
        # self.symbol_table.remove_scope()
        # print("AFTER")
        # pp.pprint(self.symbol_table.get_symbol_table())
        return ctx.returnType.text, arguments, has_error

    def visitArguments(self, ctx):
        arguments = []
        for arg in ctx.formal():
            returned_arguments = self.visit(arg)
            arguments.append(returned_arguments.name)
            self.symbol_table.add_symbol(returned_arguments.name, returned_arguments.type, size=self.type_table.get_size(returned_arguments.type))
        return arguments

    def visitFormal(self, ctx):
        self.type_table.add_argument(ctx.name.text, ctx.typeName.text)
        return Formal(ctx.name.text, ctx.typeName.text)

    def visitMultipleExpr(self, ctx):
        return_types = []
        final_code = ""
        for eachExpr in ctx.expr():
            expr = self.visit(eachExpr)
            return_types.append(expr)
            final_code += (expr.code if expr.code is not None else "")
            # print(f"Adding code{expr.code}")
        type_to_return = return_types[-1]
        type_to_return.code = final_code
        return TreeReturn("Error") if sum(check_for_errors(return_types)) else type_to_return

    # TODO Pensar retorno de multipleExpr
    def visitExpr(self, ctx):
        method_return = None
        is_bool = False
        operations_result = self.visit(ctx.operations())
        has_method_call = operations_result[0]
        result = operations_result[1]
        has_call = operations_result[2]
        operator = operations_result[3]
        if ctx.nextExpr:
            if not has_method_call:
                if result.type == "Error":
                    print(f"ERROR in line {ctx.start.line} right side expected Int found {result.type}")
                    return TreeReturn("Error")
            else:
                method_return = result
            if result.type == "Bool":
                is_bool = True
        if ctx.stringE:
            return TreeReturn("String") if not is_bool else TreeReturn("Bool")
        if ctx.ifE:
            if_expr = self.visit(ctx.ifE)
            return if_expr if not is_bool else TreeReturn("Bool", code=if_expr.code)
        if ctx.whileE:
            while_expr = self.visit(ctx.whileE)
            return while_expr if not is_bool else TreeReturn("Bool")
        if ctx.parenE:
            result = self.visit(ctx.parenE)
            return result if not is_bool else TreeReturn("Bool")
        if ctx.innerExpr:
            return self.visit(ctx.innerExpr) if not is_bool else TreeReturn("Bool")
        if ctx.calls:
            return_type = self.visit(ctx.calls)
            if has_method_call:
                new_label = self.get_new_label()
                if has_call:
                    code = f"{result.code}"
                    return_type.code = code
                else:
                    code = f"{result.code}\n{return_type.code}\n{new_label} = {return_type.addr} {operator} {result.addr}"
                    return_type.code = code
                return_type.addr = new_label
                return return_type if not is_bool else TreeReturn("Bool", addr=new_label, code=code)
            else:
                if method_return:
                    return method_return if not is_bool else TreeReturn("Bool")
                return return_type if not is_bool else TreeReturn("Bool")
        if ctx.let:
            return self.visit(ctx.let) if not is_bool else TreeReturn("Bool")
        if ctx.isVoid:
            return self.visit(ctx.isVoid) if not is_bool else TreeReturn("Bool")
        if ctx.notE:
            result = self.visit(ctx.notE)
            if not check_types(result, TreeReturn("Bool")):
                print(f"ERROR in line {ctx.start.line} expected bool, got {result.type}")
            return result if not is_bool else TreeReturn("Bool")
        if ctx.newDeclaration:
            result_decl = self.visit(ctx.newDeclaration)
            result_decl.addr = "getPointer()"
            return result_decl if not is_bool else TreeReturn("Bool")
        if ctx.boolE:
            result = self.visit(ctx.boolE)
            return TreeReturn("Bool", addr=result, code="") if not is_bool else TreeReturn("Bool")
        if ctx.intE:
            if has_method_call:
                # print(f"Result is {result}")
                new_label = self.get_new_label()
                code = f"{result.code}\n{new_label} = {ctx.intE.text} {operator} {result.addr}"
                # print(f"THIS CODE GAVE {ctx.intE.text} op {result.addr}")
                return TreeReturn("Int", addr=new_label, code=code) if not is_bool else TreeReturn("Bool", addr=new_label, code=code)
            else:
                return TreeReturn("Int", addr=ctx.intE.text, code="") if not is_bool else TreeReturn("Bool")
        if ctx.negation:
            result = self.visit(ctx.negation)
            if not check_types(result, TreeReturn("Int")):
                print(f"ERROR in line {ctx.start.line} expected Int, got {result.type}")
            return result if not is_bool else TreeReturn("Bool")
        if ctx.selfE:
            return TreeReturn("SELF_TYPE") if not is_bool else TreeReturn("Bool")
        return TreeReturn("N/A")

    def visitBoolExpr(self, ctx):
        if ctx.trueE:
            return ctx.trueE.text
        return ctx.falseE.text

    def visitNotEmpty(self, ctx):
        # print(f"{ctx} has")
        if ctx.rightSide:
            operator = ctx.getChild(0).getText()
            result = self.visit(ctx.rightSide)
            if ctx.equal or ctx.lower or ctx.greater or ctx.lowerE or ctx.greaterE:
                return True, TreeReturn("Bool", addr=result.addr, code=result.code), False, operator
            else:
                return True, TreeReturn("Int", addr=result.addr, code=result.code), False, operator
            return True, result, False
        if ctx.mCall:
            # print(f"MCall returned {self.visit(ctx.mCall)}")
            return True, self.visit(ctx.mCall), True, ""

    def visitMethodCall(self, ctx):
        # print(f"Visiting {ctx.methodName.text}")
        if ctx.methodName.text not in self.type_table.get_methods():
            print(f"ERROR in line {ctx.start.line} method {ctx.methodName.text} does not exist")
            return TreeReturn("Error")
        if ctx.heritage:
            h_result = self.visit(ctx.heritage)
            if check_types(h_result, TreeReturn("Error")):
                print(f"ERROR in line {ctx.start.line} does not inherit")
        method_arguments = self.type_table.get_methods()[ctx.methodName.text]['arguments']
        method_types = [self.type_table.get_arguments()[method_type]['type'] for method_type in method_arguments]
        actual_types = []
        actual_returns = []
        for expr in ctx.expr():
            actual = self.visit(expr)
            actual_returns.append(actual)
            actual_types.append(actual.type)
        is_correct_size = len(method_arguments) == len(actual_types)
        is_correct_type = np.array_equal(method_types, actual_types)
        has_correct_args = is_correct_size and is_correct_type
        param_code = "\n"
        for actual_return in actual_returns:
            param_code += f"{actual_return.code}\nparam {actual_return.addr}\n"
        # print(f"Final code {param_code}")
        if not has_correct_args:
            print(f"ERROR in line {ctx.start.line} method {ctx.methodName.text} has incorrect arguments")
        # print(f"Method {ctx.methodName.text} has arguments {method_arguments} of type {method_types} and actual args {actual_types} and is correct: {has_correct_args}")
        return TreeReturn(self.type_table.get_methods()[ctx.methodName.text]['return_type'], code=f"{param_code}CALL {ctx.methodName.text}, {len(actual_returns)}")

    def visitAtOperator(self, ctx):
        parent_name = ctx.parentName.text
        found = self.type_table.type_exists(parent_name)
        return TreeReturn("Valid") if found else TreeReturn("Error")

    def visitEscape(self, ctx):
        return False, TreeReturn("Escaped"), False, ""

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIfExpr(self, ctx):
        condition_type = self.visit(ctx.cond)
        then_type = self.visit(ctx.thenExpr)
        else_type = self.visit(ctx.elseExpr)
        if_label = self.get_new_if()
        else_label = self.get_new_if()
        # print(f"GOTO {else_label}")
        # print(f"IF:{then_type}")
        # print(f"{else_label}: {else_type.code}")
        has_if_error = check_types(condition_type, TreeReturn("Error")) or not check_types(condition_type, TreeReturn("Bool"))
        has_then_error = check_types(then_type, TreeReturn("Error"))
        has_else_error = check_types(else_type, TreeReturn("Error"))
        return_label = self.get_new_label()
        code = f"\n{condition_type.code}\n{condition_type.addr} GOTO {if_label}\nGOTO {else_label}\n{if_label}:{then_type.code}\n{return_label}={then_type.addr}\n{else_label}:{else_type.code}\n{return_label}={else_type.addr}"
        # code = ""
        has_error = has_if_error or has_then_error or has_else_error
        if has_if_error:
            print(f"ERROR in line {ctx.start.line} conditional not Bool")
        if has_then_error:
            print(f"ERROR in line {ctx.start.line} then expression is invalid")
        if has_else_error:
            print(f"ERROR in line {ctx.start.line} else expression is invalid")
        if has_error:
            return TreeReturn("Error")
        if check_types(else_type, then_type) and else_type.type != "Valid":
            else_type.code = code
            else_type.addr = return_label
            return else_type
        return TreeReturn("Object", code=code, addr=return_label)

    def visitWhileExpr(self, ctx):
        condition_type = self.visit(ctx.cond)
        main_type = self.visit(ctx.mainExpr)
        has_cond_error = check_types(condition_type, TreeReturn("Error")) or not check_types(condition_type, TreeReturn("Bool"))
        has_main_error = check_types(main_type, TreeReturn("Error"))
        has_error = has_cond_error or has_main_error
        while_cond_label = self.get_new_while()
        while_label = self.get_new_while()
        while_escape_label = self.get_new_while()
        code = f"\n{while_cond_label}:\n{condition_type.code}\n{condition_type.addr} GOTO {while_label}\nGOTO {while_escape_label}\n{while_label}:{main_type.code}\nGOTO {while_cond_label}\n{while_escape_label}:"
        if has_cond_error:
            print(f"ERROR in line {ctx.start.line} conditional not Bool")
        if has_main_error:
            print(f"ERROR in line {ctx.start.line} main expression is invalid")
        return TreeReturn("Error") if has_error else TreeReturn("Object", code=code)

    def visitNotExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIsVoidExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitOverwrite(self, ctx):
        parent_class = None
        if self.inherits_from:
            if self.inherits_from in self.type_table.get_classes():
                parent_class = self.type_table.get_classes()[self.inherits_from]
            else:
                print(f"ERROR in line {ctx.start.line} class does not exist")
                return TreeReturn("ERROR")
        if not self.check_symbol_table(ctx.name.text) and not self.type_table.exists_in_parent(self.inherits_from, ctx.name.text):
            pp.pprint(self.symbol_table.get_symbol_table())
            # print(f"Class {ctx.name.text} inherits {self.type_table.exists_in_parent(self.inherits_from, 'currentStation')}")
            print(f"ERROR in line {ctx.start.line} {ctx.name.text} in class {self.current_class} not defined")
            return TreeReturn("Error")
        if ctx.attr:
            actual_type = self.visit(ctx.attr)
            # print(f"Visiting one overwrite {actual_type}")
            symbol_table = self.symbol_table.find_symbol(ctx.name.text)
            pointer = self.symbol_table.get_pointer(ctx.name.text)
            if check_types(TreeReturn(symbol_table), actual_type):
                actual_type.code = f"{actual_type.code}\nB[{pointer}] = {actual_type.addr}"
                actual_type.addr = f"B[{pointer}]"
                return actual_type
            else:
                print(f"ERROR in line {ctx.start.line} declared type {symbol_table} does not match actual_type")
                return TreeReturn("Error")
        if ctx.fun:
            return_type = self.symbol_table.find_symbol(ctx.name.text)
            parameters_whole = self.visit(ctx.fun)
            parameters = parameters_whole[0]
            param_code = f"\n{parameters_whole[1]}"
            parameters_types = [self.symbol_table.find_symbol(i) for i in parameters]
            # print(f"Calling function {ctx.name.text} with parameters {parameters}")
            declared_params = []
            declared_types = []
            if not self.symbol_table.check_for_symbol(ctx.name.text):
                declared_params = self.type_table.get_methods()[ctx.name.text]['arguments']
                declared_types = [self.type_table.get_arguments()[i]['type'] for i in declared_params]
            else:
                declared_params = self.symbol_table.get_params(ctx.name.text)
                declared_types = [self.symbol_table.find_symbol(i) for i in declared_params]
            # print(f"Calling function with parameters {self.symbol_table.get_params(ctx.name.text)} of type {declared_types}")
            has_correct_length = len(parameters) == len(declared_params)
            has_correct_types = np.array_equal(parameters, declared_types)
            # print(f"{parameters} {declared_params}")
            is_correct = has_correct_types and has_correct_length
            if not is_correct:
                print(f"ERROR in line {ctx.start.line} function {ctx.name.text} has wrong signature")
            return_label = self.get_new_label()
            return TreeReturn(return_type, code=f"\n{param_code}\n{return_label} = CALL, {len(parameters)} {ctx.name.text}\n", addr=return_label)
        if not (ctx.attr or ctx.fun):
            offset = self.symbol_table.get_pointer(ctx.name.text)
            return TreeReturn(self.symbol_table.find_symbol(ctx.name.text), addr=f"B[{offset}]", code="")
        return

    def visitFunCall(self, ctx):
        arguments = []
        code = "\n"
        for oneExpr in ctx.expr():
            result = self.visit(oneExpr)
            code += f"{result.code}\nparam {result.addr}"
            arguments.append(result.type)
        return arguments, code

    def visitLetExpr(self, ctx):
        self.symbol_table.add_scope()
        code = "\n"
        exprs = []
        for argExpr in ctx.initialExpr():
            arg_result = self.visit(argExpr)
            code += f"{arg_result.code}"
            exprs.append(arg_result)
        result = self.visit(ctx.mainExpr)
        result.code = f"{code}\n{result.code}"
        values = check_types(result, TreeReturn("Error"))
        self.symbol_table.remove_scope()
        return TreeReturn("Error") if values else result

    def visitDeclaration(self, ctx):
        if ctx.typeName.text not in self.type_table.get_classes():
            print(f"ERROR in line {ctx.start.line} {ctx.typeName.text} does not exist")
        return TreeReturn(ctx.typeName.text)

    def visitInitialExpr(self, ctx):
        self.symbol_table.add_symbol(ctx.name.text, ctx.typeName.text, size=self.type_table.get_size(ctx.typeName.text))
        print('Symbol table')
        # pp.pprint(self.symbol_table.get_symbol_table())
        if ctx.actualExpr:
            actual_type = self.visit(ctx.actualExpr)
            has_error = not check_types(actual_type, TreeReturn(ctx.typeName.text)) or actual_type.type == "Error"
            if has_error:
                print(f"ERROR in line {ctx.start.line} declared type does not match actual type")
            return TreeReturn("Error") if has_error else TreeReturn("Valid", code=f"{actual_type.code}\nB[{self.symbol_table.get_pointer(ctx.name.text)}]={actual_type.addr}", addr=actual_type.addr)
        return TreeReturn("Valid")

    def visitAttrWrite(self, ctx):
        return_type = self.visit(ctx.attrInner)
        return return_type

class PongApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='horizontal')
        # LEFT LAYOUT
        self.left_layout = BoxLayout(orientation='vertical')
        self.left_input = TextInput(text="""""", multiline=True)
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
        print("-------------STARTING NEW COMPILATION-------------")
        output = visitor.visit(tree)
        print(F"OUTPUT{output}")


if __name__ == "__main__":
    PongApp().run()
