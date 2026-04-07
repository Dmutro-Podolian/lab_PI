def board_space(n, w, h):
    min_num = custom_max(w, h)
    max_num = custom_max(w, h) * n
    result = max_num
    it = 0

    while min_num <= max_num:
        it+=1
        if max_num !=0:
            average = (min_num + max_num) // 2
            count = (average // w) * (average // h)
        else:
            print("довжина і висота листка не можу бути 0")

        if count >= n:
            result = average
            max_num = average - 1
        else:
            min_num = average + 1
    print(it)

    return result

def custom_max(a, b):
    if a >= b:
        return a
    else:
        return b