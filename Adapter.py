class OldSystem:
    def old_method(self):
        return "Old"

class Adapter:
    def __init__(self, obj):
        self.obj = obj

    def new_method(self):
        #print("new features")
        return self.obj.old_method()

o=OldSystem()
a=Adapter(o)
print(a.new_method())