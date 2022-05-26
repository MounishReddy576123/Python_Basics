# Four Ways of implementing polymorphism
#Duck Typing
#Operator Overloading
#Method Overloading
#Method Overriding
## Duck Typing
class PyCharm:
    def exec(self):
        print("Compiling")
        print("Running")
class VSCode:
    def exec(self):
        print("HTML Editor")
        print("CSS Editor")
        print("Compiling")
        print("Running")
class CodeEditor:
    def code(self,ide):
        ide.exec()
vs=VSCode()
ed=CodeEditor()
ed.code(vs)




