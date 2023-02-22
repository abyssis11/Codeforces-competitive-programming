rules = {
    'A': '00',
    'B': '01',
    'C': '10',
    'D': '11'
}

inp = input()
output = ''

for c in inp:
    output += rules[c]

print(output)