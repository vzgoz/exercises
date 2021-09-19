import re

text = "some@gb.ru"

pattern_domain = re.compile(r'\b\@\w+.+')
pattern_name = re.compile(r'\b\w+\b')
result = pattern_domain.findall(text)
result_name = pattern_name.findall(text)
print(result)
print(result_name[0])
