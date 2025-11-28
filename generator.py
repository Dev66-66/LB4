def filter_file(filename, keyword):
    with open(filename, 'r') as file:
        for ln in file:
            if keyword in ln:
                yield ln.strip()

print("Lines containing 'cat':")
for line in filter_file('text.txt', 'cat'):
    print(f" - {line}")