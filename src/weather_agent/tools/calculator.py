class Calculate:
    def __init__(self) -> None:
        pass
    @property    
    def name(self):
        return "calculator"
    
    @property    
    def description(self):
        return "The simple addition of two numbers"

    def execute(self,a,b):
        return a+b
