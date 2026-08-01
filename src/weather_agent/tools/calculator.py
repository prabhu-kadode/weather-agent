class Calculate:
    def __init__(self) -> None:
        pass
    @property    
    def name(self):
        return "calculator"
    
    @property    
    def description(self):
        return "The simple addition of two numbers"
    
    @property
    def parameters(self):
        return {
            "a": {
                "type": "number"
            },
            "b": {
                "type": "number"
            }
        }

    def execute(self,a,b):
        return a+b
