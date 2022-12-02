def count(a: str):
	string_dictionary = {x: a.count(x) for x in a}
	return string_dictionary


str1 = "hello"
print(count(str1))