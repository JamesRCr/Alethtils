from timer import timer


@timer(iterations=5, save=True, verbose=True, precision=6)
def factorial(n: int):
    results = [1]
    for i in range(2, n + 1):
        results.append(results[0] * i)
        del results[0]
    return results[0]


if __name__ == '__main__':
    factorial(100000)
