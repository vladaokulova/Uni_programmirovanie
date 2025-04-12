import sys


def get_mean_size():
    lines = sys.stdin.readlines()[1:]

    file_sizes = []
    for line in lines:
        try:
            size = int(line.split()[4])
            file_sizes.append(size)
        except (IndexError, ValueError):
            continue

    if not file_sizes:
        return 0

    return sum(file_sizes) / len(file_sizes)


if __name__ == "__main__":
    print(get_mean_size())
