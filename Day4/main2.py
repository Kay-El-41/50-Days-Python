def word_index(words_list: list):
    longest_word = ""
    longest_word_count = 0
    for i in words_list:
        if len(i) > longest_word_count:
            longest_word_count = len(i)
            longest_word = i
        elif len(i) == longest_word_count:
            longest_word = words_list[0]
    return words_list.index(longest_word)


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words2))
