import sys


def decrypt(message):
    result = []
    i = 0

    while i < len(message):
        if i + 1 < len(message) and message[i + 1] == '.':
            if i + 2 < len(message) and message[i + 2] == '.':
                # Удаляем предыдущий символ
                if result:
                    result.pop()
                i += 2
            else:
                # Оставляем текущий символ
                result.append(message[i])
                i += 2
        else:
            result.append(message[i])
            i += 1

    return ''.join(result)


if __name__ == "__main__":
    message = sys.stdin.read().strip()
    print(decrypt(message))
