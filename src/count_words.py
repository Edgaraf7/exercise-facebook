from collections import Counter


def count_words(words: list[str], chars: str) -> int:
    total_length = 0
    char_count = Counter(chars)

    for word in words:
        word_count = Counter(word)
        if all(word_count[char] <= char_count[char] for char in word):
            total_length += len(word)

    return total_length


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(count_words(words, chars))

    words = ["hello", "world", "students"]
    chars = "welldonehoneyr"
    print(count_words(words, chars))
