import re
def main () :
    with open("books/frankenstein.txt") as f :
        file_contents = f.read()
    
    def to_string (file) :
        count = len(file.split())
        return count
    


    def letter_count (file):
        letters = {}
        to_lower = file.lower()
        half_split = to_lower.split()
        sorting_list = []
        for word in half_split :
            for letter in word :
                sorting_list.append(letter)
        new_sorted_list = sorted(sorting_list)
        clean_text = ''.join(char for char in new_sorted_list if char.isalpha())
        sorting_list.clear()
        for letter in clean_text :
            if letter in letters :
                letters[f"{letter}"] += 1
            else :
                letters[f"{letter}"] = 1


            
        return letters
    


        

    letters_counted = letter_count(file_contents)
    words_counted =  to_string(file_contents)
    
   
    
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counted} words found in the document")
    print("       ")
    print("       ")
    for item in letters_counted :
        print(f"The {item} character was found {letters_counted[item]} times")
    print("--- End report ---")
    
    

        


main()
