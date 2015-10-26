import math, time
from copy import deepcopy
from pprint import pprint

class Anagrams():
    def __init__(self):
        # we create a hash table sized 14 bits to 5381
        self.hash_table_size = 5381 << 14
        self.hash_table = [''] * self.hash_table_size

        # collision management
        self.collision_list = []

    # find all anagrams for words in the file
    def find_all_anagrams(self, file):
        f = open(file, 'r')
        for word in f.readlines():
            d = {}
            word = word.strip('\n')
            # find anagrams for a word
            anagrams = self.find_anagrams(word)
            # add anagrams to the hash table for the file
            hash = self.get_hash(word)
            while(self.hash_table[hash] != ''):
                if self.hash_table[hash] == word:
                    d[word] = anagrams
                    self.hash_table[hash] = d
                else:
                    hash += 1
        f.close()
        return self.hash_table

    # find anagrams for a word
    def find_anagrams(self, word):
        anagrams = []
        # create permutations
        permutations = self.get_permutations(word)
        for word in permutations:
            # get the hash code for word
            hash = self.get_hash(word)
            # check in hash table? append:
            while(self.hash_table[hash] != ''):
                if self.hash_table[hash] == word:
                    anagrams.append(word)
                    break
                else:
                    hash += 1
        # anagrams found
        return anagrams
            
    # find all the permutations for a word
    def get_permutations(self, word):
        # n!/(n-k)! = n! in this case
        # TODO
        permutations = []
        word = list(word)

        return permutations

    # build hash table from a dictionary of 350,000 words
    def build_hash_table(self, file):
        f = open(file, 'r')
        # populate hash table
        for word in f.readlines():
            word = word.strip('\n')
            hash = self.get_hash(word)

            if self.hash_table[hash] != '':
                self.add_collision(hash, word)
            else:
                self.hash_table[hash] = word

        f.close()
        return self.hash_table

    # DJB2 hash function used for lesser collisions
    def get_hash(self, string):
        hash = 5381
        for i in range(0, len(string)):
            hash = ((hash << 5) + hash) + ord(string[i])
        return hash % self.hash_table_size

    # adding collisions using linear probing
    def add_collision(self, hash, word):
        hashcode = hash
        while(self.hash_table[hashcode] != ''):
            hashcode += 1
            self.collision_list.append(word)
        self.hash_table[hashcode] = word
        return hashcode

# MAIN
# 1. Find all the permutations
# 2. Find hash code of all permutations
# 3. Cross check with Hash table of dictionary.txt
# 4. Maybe add a cross checker with same alphabets
if __name__ == '__main__':
    start = time.clock()
    print "Start: " , start
    d = "dictionary.txt"
    t = "dict1"

    A = Anagrams()
    # build table
    A.build_hash_table(d)
    # find permutations
    A.find_anagrams(t)
    # collisions range 2-3
    print len(A.collision_list)
    print "End: " , time.clock() - start
