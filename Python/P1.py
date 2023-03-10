def is_anagram(str1, str2):

    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    if len(str1) != len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    return sorted_str1 == sorted_str2

print(is_anagram('ankit','tikna'))