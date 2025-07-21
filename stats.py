def word_count(file_contents):

    word_list = file_contents.split()
    
    word_count = len(word_list)

    return word_count

def char_count(file_contents):
   
    characters = {}
    for i in file_contents:
        ch = i.lower()
        if ch in characters:
            characters[ch] += 1

        else:
            characters[ch] = 1

    return characters

def sort_on(char_sort):

    stats_list = []

    for char, num in char_sort.items():

        sorted_dict = {"char": char, "num": num}

        stats_list.append(sorted_dict)

    stats_list.sort(reverse=True, key=lambda d: d["num"])

    return stats_list
