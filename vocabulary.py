def add_prefix_un(word):

    return "un" + word


def make_word_groups(vocab_words):
    

    prefix = vocab_words[0]
    return prefix + " :: " + " :: ".join([prefix + word for word in vocab_words[1:]])

   


def remove_suffix_ness(word):

    new_word = word[:-4]
    if new_word.endswith("i"):
        new_word = new_word[:-1]
        new_word = new_word + "y"
        return new_word
    else:
        return new_word
        
def adjective_to_verb(sentence, index):

    word_verb = sentence.split()[index]
    if word_verb[-1] == "." or word_verb[-1] == "!" or word_verb[-1] == ",":
        word_verb = word_verb[:-1]
        verb = word_verb + "en"
    else:
        verb = word_verb + "en"
    return verb
        
        

