def star(n):
    if n == 1:
        return ['*']

    pattern = star(n // 3)
    result = []

    for line in pattern:
        result.append(line * 3)
    for line in pattern:
        result.append(line + ' ' * (n // 3) + line)
    for line in pattern:
        result.append(line * 3)

    return result

n = int(input())
stars = star(n)
for line in stars:
    print(line)
