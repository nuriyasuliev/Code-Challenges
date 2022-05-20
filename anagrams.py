def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)
print(is_anagram('honey', 'bunny'))
print(is_anagram('boat', 'coat'))