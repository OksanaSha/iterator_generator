
class FlatIterator:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.cursor = -1
        self.iter_stack = [iter(self.lst)]
        return self

    def __next__(self):
        while self.iter_stack:
            try:
                value = next(self.iter_stack[-1])
            except StopIteration:
                self.iter_stack.pop()
                continue
            if isinstance(value, list):
                self.iter_stack.append(iter(value))
            else:
                return value
        raise StopIteration


def flat_generator(lst):
    for val in lst:
        if isinstance(val, list):
            for item in flat_generator(val):
                yield item
        else:
            yield val

nested_list = [
	['a', 'b', 'c'], 1, [[[3], 4], 5],
	['d', 'e', 'f', 'h', False],
	[1, 2, None], 6, [7]
]

print('generator')
for item in flat_generator(nested_list):
    print(item)
print('------')

print('iterator')
for item in FlatIterator(nested_list):
    print(item)


