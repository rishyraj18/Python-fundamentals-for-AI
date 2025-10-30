class MathOps:

    @staticmethod
    def add(x,y):
        return (f"The sum of {x} and {y} is {x+y}")
    
    @staticmethod
    def is_even(n):
        return (f"is the number {n} is even {'yes' if n%2 == 0 else 'no'}")
    
    @staticmethod
    def squared(n):
        return (f"Square of {n} : {n**2}")
    

print(MathOps.add(10,2))
print(MathOps.is_even(7))
