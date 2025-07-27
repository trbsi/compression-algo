def saveToImage():
    with open("image.bin", "rb") as file:
        binaryData = file.read()

    with open("image.jpg", "wb") as f:
        f.write(binaryData)


def saveToBin():
    with open("MainBefore.jpg", "rb") as image:
        data = image.read()

    with open("image.bin", "wb") as image:
        image.write(data)


def main():
    task = input("Enter the name of the task: tobin or tojpg: ")
    if task == "tobin":
        saveToBin()

    if task == "tojpg":
        saveToImage()


if __name__ == "__main__":
    main()
