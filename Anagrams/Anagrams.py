import math, time
from copy import deepcopy

class Anagrams():
    def __init__(self):
        # we create a hash table sized 15 bits to 5381
        self.hash_table_size = 5381 << 14
        self.hash_table = [''] * self.hash_table_size
        # collision management
        self.collision_list = []

    def build_hash_table(self, file):
        counter = 0
        f = open(file, 'r')
        # populate hash table
        for word in f.readlines():
            counter += 1
            hash = self.get_hash(word)
            if self.hash_table[hash] != '':
                self.collision_list.append(word)
            else:
                self.hash_table[hash] = word
        f.close()

    # DJB2 hash function used for lesser collisions
    def get_hash(self, string):
        hash = 5381
        for i in range(0, len(string)):
            hash = ((hash << 5) + hash) + ord(string[i])
        return hash % self.hash_table_size

# MAIN
# 1. Find all the permutations
# 2. Find hash function of all permutations
# 3. Cross check with Hash table of dictionary.txt
if __name__ == '__main__':
    start = time.clock()
    print "Start: " , start
    d = "dictionary.txt"
    A = Anagrams()
    #print A.get_hash("stop")
    A.build_hash_table(d)
    print len(A.collision_list)
    print "End: " , time.clock() - start
