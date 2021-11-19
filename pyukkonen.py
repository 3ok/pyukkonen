def ukkonen(a: str, b: str, threshold: int) -> int:
    if a == b:
        return 0

    if len(a) > len(b):
        a, b = b, a

    a_len = len(a)
    b_len = len(b)

    while a_len > 0 and a[a_len - 1] == b[b_len - 1]:
        a_len -= 1
        b_len -= 1

    if a_len == 0:
        return min(b_len, threshold)

    t_start = 0
    while t_start < a_len and a[t_start] == b[t_start]:
        t_start += 1

    a_len -= t_start
    b_len -= t_start

    if a_len == 0:
        return min(b_len, threshold)

    threshold = min(b_len, threshold)
    d_len = b_len - a_len
    if threshold < d_len:
        return threshold

    ZERO_K = min(a_len, threshold) // 2 + 2
    array_size = d_len + ZERO_K * 2 + 2
    current_row = array_size * [-1]
    next_row = array_size * [-1]

    i = 0
    condition_row = d_len + ZERO_K
    end_max = condition_row * 2

    while True:
        i += 1

        current_row, next_row = next_row, current_row
        current_cell = -1
        if i <= ZERO_K:
            start = -i + 1
            next_cell = i - 2
        else:
            start = i - (ZERO_K * 2) + 1
            next_cell = current_row[ZERO_K + start]

        if i <= condition_row:
            end = i
            next_row[ZERO_K + i] = -1
        else:
            end = end_max - i

        for k in range(start, end):
            row_index = k + ZERO_K
            previous_cell = current_cell
            current_cell = next_cell
            next_cell = current_row[row_index + 1]

            t = max(current_cell + 1, previous_cell, next_cell + 1)
            while (
                t + t_start < a_len
                and t + k + t_start < b_len
                and a[t_start + t] == b[t_start + t + k]
            ):
                t += 1

            next_row[row_index] = t

        if not (next_row[condition_row] < a_len and i <= threshold):
            break

    return i - 1
