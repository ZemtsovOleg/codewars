def make_class(*args):
    class MyClass:
        def __init__(self, *values):
            for arg, value in zip(args, values):
                setattr(self, arg, value)
    return MyClass


Animel = make_class("name", "species", "age", "health", "weight", "color")
dog1 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")
