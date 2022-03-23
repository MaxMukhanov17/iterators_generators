class FlatIterator:
	def __init__(self, nested_list):
		self.nested_list = nested_list

	def unific_lists(self):
		flat_list = []
		for nest_list in self.nested_list:
			for elements in nest_list:
				flat_list.append(elements)
		return flat_list

	def __iter__(self):
		return iter(self.unific_lists())

	def __next__(self):
		if len(self.unific_lists) == 0:
			raise StopIteration

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

flat_iterator = FlatIterator(nested_list)

flat_list = [item for item in flat_iterator]
print(flat_list)

for item in flat_iterator:
	print(item)