import re

text = 'Cats are smarter than dogs'

a = re.match(r'(.*) are (.*?) .*', text, re.M | re.I)

if a :
    print('a.group()', a.group())
    print('a.group(1)', a.group(1))
    print('a.group(2)', a.group(2))
else:
    print('GG')


text = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = text.match('Hello World Wide Web')
print(m)
print(m.group())
print(m.span())
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
