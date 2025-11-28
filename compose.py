def compose(*functions):
    def composes(x):
        res = x
        for func in functions:
            res = func(res)
        return res
    return composes

def plus(x):
    return x + 1

def square(x):
    return x ** 2

def multiplication(x):
    return x * 2

composed = compose(plus, square, multiplication)
result = composed(2)
print(result)