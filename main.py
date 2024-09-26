def main ():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = count_words(text)
    counted_characters = character_count(text)
    counted_characters.sort(reverse=True, key=sort_on)
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for individual in counted_characters:
        print(f"The '{individual['Character']}' character was found {individual['Count']} times")

    

def count_words(text):
    words= text.split()
    return len(words)

def book_text(path):
    with open(path) as f:
        return f.read()

    
def character_count(text):
    lowered = text.lower()
    character_count = {}
    
    
    for i in lowered:
        if i.isalpha():
            if i in character_count :
                character_count[i] += 1
            else :
                character_count[i] = 1
    character_list = []


    for n in character_count:
        separated_dict = {}
        separated_dict["Character"] = n
        separated_dict["Count"] = character_count[n]
        character_list.append(separated_dict)
    return character_list

def sort_on(dict):
    return dict["Count"]









    
main()
