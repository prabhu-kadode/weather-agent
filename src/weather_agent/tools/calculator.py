class Calculate:
    def __init__(self) -> None:
        self.operations = {
            "addition": self.add,
            "multiplication": self.mul,
            "division": self.div,
            "substraction": self.sub,
        }

    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return "The simple calculator and it has actions like addition,multiplication ,substraction,division"

    @property
    def parameters(self):
        return {
            "a": {"type": "number"},
            "b": {"type": "number"},
            "action": {
                "type": "string",
                "enum": ["addition", "multiplication", "substraction", "division"],
            },
        }

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a / b

    def execute(self, a, b, action):
        op = self.operations.get(action)
        return op(a, b)
        # if action =='addition':
        #     return a+b
        # elif action == "multiplication":
        #     return a*b
        # elif action == 'substraction':
        #     return a-b
        # elif action == "division":
        #     return a/b
