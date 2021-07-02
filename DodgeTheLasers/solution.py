from decimal import Decimal, getcontext


def solution(s):
    # Set precision of decimal values to 101 to ensure that precision isnt lost
    getcontext().prec = 101
    n = int(s)
    r = Decimal(2).sqrt()

    modifier = 1
    total = 0

    # Beatty sequence!
    # Repeat until n has fallen to zero
    while n > 0:
        m = int((r - 1) * n // 1)
        sub_total = n * m + n * (n + 1) / 2 - m * (m + 1) / 2

        total += modifier * sub_total

        n = m
        modifier *= - 1

    total = int(total)

    return str(total)


if __name__ == "__main__":
    print(solution('77'))
    print(solution('5'))
