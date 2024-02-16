from abc import ABC,abstractmethod
class editor(ABC):
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def save(self):
        pass
class vscode(editor):
    def edit(self):
        print("vscode edit")
    def debug(self):
        print("vscode debug")
    def run(self):
        print("vscode run")
    def save(self):
        print("save")

obj=vscode()
obj.debug()
obj.save()