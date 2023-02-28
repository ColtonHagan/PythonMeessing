import string

def count_words(filename):
    words = dict()
    #This should be extended to check for other txt file extentions
    if(filename[-4:] != ".txt"):
        filename += ".txt"
    #This is should have error checks if it is a new program
    #Other is just for linking to my text files, so i have to type less, should be replaced
    with open("Other/" + filename) as file_object:
        for line in file_object:     
            for word in line.split():
                word = word.strip()
                word = word.translate(word.maketrans('', '', string.punctuation))     
                cnt = 1
                if(word in words):
                    cnt += words[word]
                words[word] = cnt
    words = sorted(words.items(), key=lambda x:x[1], reverse=True)
    return words
def main():
    filename = input("Enter the name of the text file: ")
    word_counts = count_words(filename)
    print("The ten most common words are:")
    for i in range(0, min(10, len(word_counts))):
        print(word_counts[i])

if __name__ == "__main__":
    main()