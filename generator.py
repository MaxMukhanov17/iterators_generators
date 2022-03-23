nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
    for elements in nested_list:
        if isinstance(elements, list):
            for i in elements:
                yield i
        else:
            yield elements

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)

for item in  flat_generator(nested_list):
	print(item)