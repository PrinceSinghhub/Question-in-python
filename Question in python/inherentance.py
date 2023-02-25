class pr:
    def __init__(self,name):
        self.name=name
    def team(self):
        return self.name
    def isap(self):
        return True
class codex(pr):
    def isap(self):
        print("To Kesi Hai aap Log")
        return True
p=pr("CODEX CODER")
print(p.team(),p.isap())
p=codex("Powerfull People Make Place Powerfull")
print(p.team(),p.isap())

