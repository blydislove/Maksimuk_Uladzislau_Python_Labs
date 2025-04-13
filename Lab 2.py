# def find_positions(s, t):
#     s = s.upper()
#     t = t.upper()
#     positions = []
#     if len(t) == 0 or len(t) > len(s):
#         return positions
#     for i in range(len(s) - len(t) + 1):
#         if s[i:i+len(t)] == t:
#             positions.append(str(i))
#     return positions
#
# s = input().strip()
# t = input().strip()
#
# positions = find_positions(s, t)
#
# print(' '.join(positions))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def find_positions(s, t):
    s = s.upper()
    t = t.upper()
    positions = []
    if len(t) == 0 or len(t) > len(s):
        return positions
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i)  # Теперь сохраняем как числа
    return positions


# Ввод данных и выполнение
s = input("Введите фулл последовательность:").strip()
t = input("Введите поисковую последовательность:").strip()

positions = find_positions(s, t)

# Сортировка с помощью merge sort (хотя результат уже отсортирован)
sorted_positions = merge_sort(positions)

# Преобразуем обратно в строки для вывода
print(' '.join(map(str, sorted_positions)))


## GATATATGCATATACTT
## ATAT