# Problem Set 4C
# Name: lcsm29
# Collaborators: None
# Time Spent: unknown
# version 0.11.210528 - cleaned it up a bit

import string
from ps4a import get_permutations


# HELPER CODE #
def load_words(file_name):
    """ file_name (string): the name of the file containing
        the list of words to load
    Returns: a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may take a while
    """

#    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
#    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """ Determines if word is a valid word, ignoring
    capitalization and punctuation
    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >> is_word(word_list, 'bat') returns
    True
    >> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


# END HELPER CODE #

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        """ Initializes a SubMessage object
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        """ Used to safely access self.message_text outside of the class
        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """ Used to safely access a copy of self.valid_words outside of the
            class. This helps you avoid accidentally mutating class attributes
        Returns: a COPY of self.valid_words
        """
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        """ vowels_permutation (string): a string containing a permutation 
                                         of vowels (a, e, i, o, u)
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (str) to another letter (str)
        """
        t_dict = {c: vowels_permutation[i] for i, c in enumerate(VOWELS_LOWER)}
        t_dict.update({c: c for c in CONSONANTS_LOWER})
        t_dict.update({c.upper(): t_dict[c].upper() for c in t_dict.copy()})
        return t_dict

    def apply_transpose(self, transpose_dict):
        """ transpose_dict (dict): a transpose dictionary
        Returns: an encrypted version of the message text, based on the dict
        """
        return ''.join([transpose_dict[c] if c in transpose_dict.keys() 
                        else c for c in self.message_text])


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        """ Initializes an EncryptedSubMessage object
        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        """ Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        """
        candidates = {perm: [self.build_transpose_dict(perm), 0]
                      for perm in get_permutations('aeiou')}
        for dict_hitcount_lst in candidates.values():
            for word in self.apply_transpose(dict_hitcount_lst[0]).split():
                if is_word(self.get_valid_words(), word):
                    dict_hitcount_lst[1] += 1
        best = max(candidates.values(), key=lambda x: x[1])
        return self.message_text if best[1] == 0 else self.apply_transpose(best[0])


if __name__ == '__main__':
    def printer(msg, perm, expected):
        message = SubMessage(msg)
        permutation = perm
        enc_dict = message.build_transpose_dict(permutation)
        print(f"Original message: {message.get_message_text()}, Permutation: {permutation}")
        print(f"Expected encryption: {expected}")
        print(f"Actual encryption: {message.apply_transpose(enc_dict)}")
        e_msg = EncryptedSubMessage(message.apply_transpose(enc_dict))
        print(f"Decrypted message: {e_msg.decrypt_message()}\n")

    # Example test case (6/120 permutations yielded 2 hits)
    printer("Hello World!", "eaiuo", "Hallu Wurld!")

    # Single best hit case (1/120 permutation yielded 8 hits)
    m = "Easy peasy case Many simple words No special letters"
    p = "uiaoe"  
    e = "Iusy piusy cusi Muny sampli words No spicaul littirs"
    printer(m, p, e)

    # Non-alphabet characters included (4/120 perms yield 4 hits)
    m = "This is a Te$t Message a\u0430α\u00E0\u00E2\u00E4诶あ아"
    p = "ouaei"
    e = "Thas as o Tu$t Mussogu oаαàâä诶あ아"
    printer(m, p, e)

    # This depends on luck (4/120 perms yield 3 hits)
    m = "aCe OR beD"
    p = "eaoiu"
    e = "eCa IR baD"
    printer(m, p, e)

    # Zero hit case, because both words don't exist in the word.txt
    m = "Nürburgring Nordschleife"
    p = "uaoei"
    e = "Nürbirgrong Nerdschlaofa"
    printer(m, p, e)

    # Another single best hit case (5 hits)
    m = "Gigantic 640 Kilobytes Random Access Memory"
    p = "uaeio"
    e = "Geguntec 640 Kelibytas Rundim Uccass Mamiry"
    printer(m, p, e)
