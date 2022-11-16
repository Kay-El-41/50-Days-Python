def count_elements(item: str):
    new = item.split()
    count = 0
    for j in new:
        count += len(j)
    print(f"{count} elements.")


def count_words(item: str):
    print(f"{len(item.split())} words")
    count_elements(item)


count_words("I love learning")

