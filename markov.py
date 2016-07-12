from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string.rstrip()

print open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    value = []

    #loop over the words in our string
    words = text_string.split()
    for i in range(len(words)-2): #-2 will stop after Sam I which is the last key we want 
        print i
        # word_pair = words[i], words[i+1]
    
    #add each word to the empty dictionary (even and odd word bigram)
    # chains.get(i, 0) + 1 #values as the list of strings following the tuple key 
    # print chains

    #bigrams will be the keys and the values will be every possible following word 
        current_key = (words[i], words[i+1]) #would you
        chosen_word = words[i+2] #could or like
        # new_key = (words[i+1], words[i+2]) #you could or you like

        chains[current_key] = [chosen_word]
        # print current_key
        # print chains
        # print "added a %s, %s to dict!" % (current_key[0], current_key[1])
    #print chains # this does not show mulitple values
    #if key is in dictionary:
        #append to the current value
        chains[current_key] = chains.get(current_key, None) + [chosen_word]
    #else:
        #append the key to the dictionary with the chosen value
    print chains
#need .get() to count the instances of the values, if we dont have word pair do blah
#if we do have word pair, we add current value into key pair (i.e. line 47)
    #return chains

big_block_of_words = open_and_read_file("green-eggs.txt")
print make_chains(big_block_of_words) #calling the function within the next function INCEPTION

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     text = ""

#     # your code goes here

#     return text


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
