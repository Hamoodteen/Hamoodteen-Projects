class ana :
    a = 1
    b = 2
    def __init__(self , aaa):
        self.aaa = aaa
        print(f"it is {self.aaa}")
    def __getattr__(self , attr):
        return "not found"
s = ana("zzzzz")
print(f"the {s.a}")
print(f"the {s.b}")
print(f"the {s.c}")