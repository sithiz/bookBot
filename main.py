def main () :
    with open("books/frankenstein.txt") as f :
        file_contents = f.read()
    
    def to_string (file) :
        count = len(file.split())
        return count
    print(to_string(file_contents))
    def letter_count (file):
        letters = {}
        to_lower = file.lower()
        half_split = to_lower.split()
        for word in half_split :
            for letter in word :
                if letter in letters :
                    letters[f"{letter}"] += 1
                else :
                    letters[f"{letter}"] = 0
        return letters
    

        

    print(letter_count(file_contents))
        


main()
