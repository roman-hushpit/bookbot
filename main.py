def sort_on(dict):
    return dict["value"]

def sort_dict(dict):
    list = []
    for key in dict:
        list.append({"key": key, "value": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def character_counter(text):
    letter_table = {}
    for letter in text.lower():
        if(not letter.isalpha()):
            continue
        if (letter in letter_table):
            letter_table[letter] = letter_table[letter] + 1
        else:
            letter_table[letter] = 1
    return letter_table


file_name = "frankenstein.txt"

if __name__ == '__main__':
    with open("books/" + file_name) as f:
        file_content = f.read()
        words = file_content.split()
        characters = character_counter(file_content)
        sorted_characters = sort_dict(characters)   
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        for character in sorted_characters:
            print(f"The '{character['key']}' character was found {character['value']} times")
        print("--- End report ---")

