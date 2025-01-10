def main():
    with open("books/frankenstein.txt") as f:
        #print(f.read())
        #num_words(f.read())
        #char_counts(f.read())
        text = f.read()
        print(f'--- Begin report of books/frankenstein.txt ---')
        print(f'{num_words(text)} words found in the document\n')
        alpha_order = 'abcdefghijklmnopqrstuvwxyz'
        character_count = char_counts(text)
        for alpha in alpha_order:
            print(f'The {alpha.upper()}{alpha} character was found {character_count[alpha]} times')
        print('--- End report ---')

def num_words(string):
    return len(string.split())

def char_counts(string):
    ''' --unnecessary when using alpha_order to print--
    remove_chars = ' ,().-:1234567890[]#*?;!_/%@$"\'\n' 
    for char in remove_chars:
        clean_string = clean_string.replace(char, '')
    '''

    clean_string = string.strip()
    clean_string = clean_string.lower()
    character_count = {}
    for char in clean_string:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count
    
main()