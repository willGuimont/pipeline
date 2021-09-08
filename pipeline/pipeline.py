# Some Compose and Lambda where taken from:
# https://pytorch.org/docs/stable/_modules/torchvision/transforms/transforms.html
# for a dependency-free pipeline
from typing import Callable


class Lambda:
    """
    Elevate a function into the transform structure
    """

    def __init__(self, f: Callable):
        if not callable(f):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(f).__name__)))
        self.f = f

    def __call__(self, x):
        return self.f(x)

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Identity:
    def __call__(self, x):
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Compose:
    """
    Compose two transformations
    """

    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, x):
        for t in self.transforms:
            x = t(x)
        return x

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string


class Tee:
    """
    Duplicate input
    """

    def __call__(self, x):
        return x, x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class First:
    """
    Map function to first element of a pair
    """

    def __init__(self, f: Callable):
        if not callable(f):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(f).__name__)))
        self.f = f

    def __call__(self, x):
        (a, b) = x
        return self.f(a), b

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Second:
    """
    Map function to second element of a pair
    """

    def __init__(self, f: Callable):
        if not callable(f):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(f).__name__)))
        self.f = f

    def __call__(self, x):
        (a, b) = x
        return a, self.f(b)

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Bifunctor:
    """
    Map a function to the first element of a pair and another to the other element
    """

    def __init__(self, f: Callable, g: Callable):
        if not callable(f):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(f).__name__)))
        self.f = f
        if not callable(g):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(g).__name__)))
        self.g = g

    def __call__(self, x):
        (a, b) = x
        return self.f(a), self.g(b)

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Both:
    """
    Map function to both element of a pair
    """

    def __init__(self, f: Callable):
        if not callable(f):
            raise TypeError("Argument lambda should be callable, got {}".format(repr(type(f).__name__)))
        self.f = f

    def __call__(self, x):
        (a, b) = x
        return self.f(a), self.f(b)

    def __repr__(self):
        return self.__class__.__name__ + '()'


if __name__ == '__main__':
    input_value = 7
    transform = Compose([
        Tee(),
        First(lambda x: x + 1),
        Second(lambda x: x - 1),
        Both(lambda x: x * 2),
        Bifunctor(lambda x: x // 3, lambda x: x * 2),
        Both(str),
        Lambda(lambda x: ''.join(x))
    ])

    output = transform(input_value)
    print(output)
    assert output == "524"

