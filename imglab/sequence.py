DEFAULT_SIZE = 16


def sequence(first, last, size=DEFAULT_SIZE):
    """Returns a geometric sequence of integer numbers inside an interval and with specific size as list.

    :Examples:
        >>> from imglab import sequence
        >>> sequence(100, 8192)
        [100, 134, 180, 241, 324, 434, 583, 781, 1048, 1406, 1886, 2530, 3394, 4553, 6107, 8192]
        >>> sequence(100, 8192, 1)
        [100]
        >>> sequence(100, 8192, 2)
        [100, 8192]
        >>> sequence(100, 8192, 4)
        [100, 434, 1886, 8192]
        >>> sequence(70, 60, 6)
        [70, 68, 66, 64, 62, 60]
    """
    if size <= 0: return []
    if size == 1: return [first]
    if size == 2: return [first, last]

    ratio = (last / first) ** (1 / (size - 1))

    seq = [first]
    for i in range(1, size - 1):
        seq.append(seq[i - 1] * ratio)
    seq.append(last)

    return list(map(round, seq))
