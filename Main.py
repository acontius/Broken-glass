def count_arrangements(n, pieces):
    memo = {}
    return count_arrangements_recursive(n, pieces, 0, 0, 0, memo)


def count_arrangements_recursive(n, pieces, width_sum, height_sum, mask, memo):
    if mask == (1 << n) - 1:
        return 1

    if (mask, width_sum, height_sum) in memo:
        return memo[(mask, width_sum, height_sum)]

    total_arrangements = 0

    for i in range(n):
        if (mask & (1 << i)) == 0:
            new_width_sum = max(width_sum, pieces[i][0])
            new_height_sum = max(height_sum, pieces[i][1])
            new_mask = mask | (1 << i)

            total_arrangements += count_arrangements_recursive(n, pieces, new_width_sum, new_height_sum, new_mask, memo)

            if width_sum + pieces[i][1] <= new_height_sum and height_sum + pieces[i][0] <= new_width_sum:
                total_arrangements += count_arrangements_recursive(n, pieces, new_height_sum, new_width_sum, new_mask,
                                                                   memo)

    memo[(mask, width_sum, height_sum)] = total_arrangements
    return total_arrangements



piec_num = int(input("Please Enter the number of pieces : "))
pieces = []
for _ in range(piec_num):
    piece = tuple(map(int, input().split()))
    pieces.append(piece)

# حساب کردن و چاپ تعداد حالات مختلف
result = count_arrangements(piec_num, pieces)
print(f"You can make a Square in {result} Ways")
