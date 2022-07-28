import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
import pprint

# Classes format:
# name : {name: name, attr: [attributes], methods: [methods]}
pp = pprint.PrettyPrinter(indent=4)
class MyVisitor(MyGrammerVisitor):
    def check_stacks(self, stacks, name):
        for i in stacks:
            if name in i:
                return True
        return False

    def visitProgram(self, ctx):
        self.classes = {
            'Int': {
                'name': 'Int',
            },
            'Bool': {
                'name': 'Bool'
            },
            'String': {
                'name': 'String'
            }
        }
        self.methods = {}
        self.attributes = {}
        self.symbol_table = []
        self.symbol_methods = {}
        self.symbol_attributes = {}
        # value = ctx.getText()
        # return int(value)
        self.visitChildren(ctx)
        print('Classes')
        pp.pprint(self.classes)
        # print('Methods')
        # pp.pprint(self.methods)
        # print('Attributes')
        # pp.pprint(self.attributes)
        # print('Symbol table')
        pp.pprint(self.symbol_table)
        return

    def visitClassP(self, ctx):
        self.symbol_table.append({})
        self.current_class = ctx.name.text
        self.current_methods = []
        self.current_attributes = []
        # return self.visit(ctx.expr())
        self.visitChildren(ctx)
        self.classes[self.current_class] = {'name': self.current_class, 'attributes': self.current_attributes, 'methods': self.current_methods}
        # pp.pprint(self.symbol_table)
        self.symbol_table.pop()
        return ctx.getText()

    def visitFeature(self, ctx):
        self.current_feature = ctx.name.text
        self.visitChildren(ctx)
        return ctx.name.text

    # Method format:
    # name : {name : name, args: {name: {'name': name, 'type':type}}, type: type}
    def visitMethod(self, ctx):
        self.symbol_table.append({})
        (self.symbol_table[0])[self.current_feature] = {'name': self.current_feature}
        self.current_methods.append(self.current_feature)
        self.current_arguments = {}
        self.visit(ctx.argumentList)
        self.visit(ctx.mainExpr)
        self.methods[self.current_feature] = {'name': self.current_feature, 'arguments': self.current_arguments, 'return_type': ctx.returnType.text}
        # pp.pprint(self.symbol_table)
        self.symbol_table.pop()
        return

    def visitArguments(self, ctx):
        self.visitChildren(ctx)
        return

    # Attribute format:
    # name : {name : name, type: type}
    def visitAttribute(self, ctx):
        (self.symbol_table[0])[self.current_feature] = {'name': self.current_feature}
        type_name = ctx.typeName.text
        if type_name in self.classes:
            pass
        else:
            raise NotImplemented
        # pp.pprint(self.symbol_table)
        self.attributes[self.current_feature] = {'name': self.current_feature, 'type': type_name}
        return

    def visitFormal(self, ctx):
        self.current_arguments[ctx.name.text] = {'name': ctx.name.text, 'type': ctx.typeName.text}
        return

    def visitExpr(self, ctx):
        if ctx.calls:
            self.visit(ctx.calls)
        if ctx.innerExpr:
            self.visit(ctx.innerExpr)
        if ctx.let:
            self.symbol_table.append({})
            self.visit(ctx.let)
            print('Let', self.symbol_table[0])
            self.symbol_table.pop()
        self.visit(ctx.nextExpr)
        return

    def visitMultipleExpr(self, ctx):
        self.visitChildren(ctx)
        return

    def visitLetExpr(self, ctx):
        self.visit(ctx.initial)
        return

    def visitInitialExpr(self, ctx):
        name = ctx.name.text
        type_name = ctx.typeName.text
        if type_name in self.classes:
            pass
            #Change to last
            # self.symbol_table[0][name] = type_name
        else:
            raise NotImplemented
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
        if self.check_stacks(self.symbol_table, ctx.name.text):
            # print('Found', ctx.name.text)
            pass
        else:
            raise NotImplemented
        return

    # Visit a parse tree produced by MyGrammerParser#attrWrite.
    def visitAttrWrite(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#funCall.
    def visitFunCall(self, ctx):
        return self.visitChildren(ctx)


if __name__ == "__main__":
    while 1:
        data =  InputStream("""
class Radio {
    isOn:Bool <- false;
    currentStation:Int <- 0;
    turn_on():Bool{
        isOn <- true
    };
    turn_off():Bool{
        isOn <- false
    };
    change_station(newStation : Int, som : Int): Int{
        currentStation <- max(min(newStation, 100), 0)
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
