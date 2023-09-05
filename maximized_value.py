def maximize_expression_modulo(arrays, index=0, current_value=0):
    if index == len(arrays):
        return current_value % modulo_value

    max_value = 0
    for element in arrays[index]:
        new_value = current_value + (element ** 2)
        max_value = max(max_value, maximize_expression_modulo(arrays, index + 1, new_value))

    return max_value


n, modulo_value = map(int, input().split())
arrays = []

for _ in range(n):
    array_size, *array_elements = map(int, input().split())
    arrays.append(array_elements)

result = maximize_expression_modulo(arrays)
print(result)
