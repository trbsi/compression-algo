import json


def readBytesAsString():
    with open("image.bin", "rb") as f:
        data = f.read()

    bitstring = ''.join(f'{byte:08b}' for byte in data)

    with open("image.txt", "w") as f:
        f.write(bitstring)


def fromStringToBytes():
    with open("image.txt", "r") as f:
        data = f.read()

    binary = bytes(int(data[i:i + 8], 2) for i in range(0, len(data), 8))

    with open("image.bin", "wb") as f:
        f.write(binary)


def algo():
    with open("image.txt", "r") as f:
        data = f.read()
    array = list(str(data))

    counter = 1
    total = 0
    information = {}
    splitBits = []
    # moreThan2 = 0
    # exact2 = 0
    # exact1 = 0

    for key, bit in enumerate(array):
        total += 1
        if key == 0:
            lastBit = bit
            continue

        if lastBit == bit:
            counter += 1
            splitBits.append(str(bit))
        else:
            bitCounterData = information.get(counter, {})
            repeatedTotal = bitCounterData.get("repeated_total", 0)
            information[counter] = {"number_of_bits": counter, "repeated_total": repeatedTotal + 1, }
            # if counter == 1:
            #     exact1 += counter
            # elif counter == 2:
            #     exact2 += counter
            # elif counter > 2:
            #     moreThan2 += counter
            counter = 1
            lastBit = bit
            splitBits.extend([' ', str(bit)])

    sortedArray = dict(sorted(information.items()))
    with open("dict.txt", "w") as f:
        json.dump(sortedArray, f, indent=4)

    with open("split_bytes.txt", "w") as f:
        f.write(''.join(splitBits))

    print(f'total bytes: {total}')


def main():
    task = input("0: read bytes as string\n1: from string to bytes\n2: do algo\n")
    match task:
        case "0":
            readBytesAsString()
        case "1":
            fromStringToBytes()
        case "2":
            algo()


if __name__ == "__main__":
    main()
