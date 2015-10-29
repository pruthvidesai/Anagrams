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

        # anagram list per word
        self.anagram_list = []

    # find all anagrams for words in the file
    def find_all_anagrams(self, input, output):
        outf = open(output, 'w')
        inf = open(input, 'r')
        counter = 0
        for word in inf.readlines():
            counter += 1
            if counter == 1000:
                return
            elif counter % 20 == 0:
                print counter
            word = word.strip('\n')
            # find anagrams for a word
            anagrams = self.find_anagrams(word)
            # add anagrams to the file
            outf.write(word + ": " + ", ".join(anagrams) + '\n')
        inf.close()
        outf.close()
        return 

    # find anagrams for a word
    def find_anagrams(self, word):
        if len(word) > 9:
            return [word]
        anagrams = []
        # create permutations
        permutations = self.permutation_helper(word)
        for word in permutations:
            # get the hash code for word
            hash = self.get_hash(word)
            # check in hash table? append:
            while(self.hash_table[hash] != ''):
                if self.hash_table[hash] == word and anagrams.count(word) < 1:
                    anagrams.append(word)
                    break
                else:
                    hash += 1
        # anagrams found
        return anagrams
            
    # find all the permutations for a word
    # n!/(n-k)! = n! in this case
    # if you want to make changes in the permutations
    def permutation_helper(self, word):
        if not word:
            # empty list
            return [word]
        else:
            temp = []
            # for chars in word
            for char in range(len(word)):
                # part other than 'char'
                part = word[:char] + word[char + 1:]
                # permutation for the part too
                for p in self.permutation_helper(part):
                    temp.append(word[char] + p)
            return temp

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

    def mergesort(self, input, output):
        # find all same lettered words
        pass

# MAIN
# 1. Find all the permutations
# 2. Find hash code of all permutations
# 3. Cross check with Hash table of dictionary.txt
# 4. Maybe add a cross checker with same alphabets
if __name__ == '__main__':
    start = time.clock()
    d = "dict1"
    t = "dict1"
    a = "anagram1"

    A = Anagrams()
    # build table
    A.build_hash_table(d)
    print "Hash Table: " , time.clock() - start
    # find anagrams
    print A.find_all_anagrams(t, a)
    print "End: " , time.clock() - start
