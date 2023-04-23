from hashing.murmur64_hash import bytes_to_long, murmur64
from tqdm import tqdm
import random
import secrets

class HashDict:
    """
    Initialize a dictionary of VT2 murmur64 hashes and their inverse hashes, by starting with inverse hashes

    file_path: name of file containing newline seperated words
    """

    def __init__(self, file_path):
        self._word_list = self._load_words()
        self.hashPath_dict = {}
        self.paths = []

    @staticmethod
    def _load_words():
        print("Loading words. . .")
        f = open("words.txt", "r")
        Lines = f.readlines()
        word_list = []
        for word in tqdm(Lines):
            word_list.append(word.replace("\n", "").replace("-", "").replace("'","").replace("`",""))
        return word_list
    
    def _add_hashPath_to_dict(self, hash, path):
        self.hashPath_dict[hash] = path

    @staticmethod
    def _generate_hash(path):
        return murmur64(path, True)
    
    def generate_new_path(self):
        """
        Generates and adds a new path-hash combination to dictionary
        """
        new_path = secrets.choice(self._word_list)
    
        num_of_dirs = random.randint(1,7)
        for j in range(num_of_dirs):
            tkn = [secrets.choice(self._word_list), "_"+str(random.randint(0,9))+ str(random.randint(0,9))]
            new_path = new_path + "/" + secrets.choice(tkn)
                
        num_of_tkns_filename = random.randint(1,15)
        for j in range(num_of_tkns_filename):
            tkn = [secrets.choice(secrets.choice(self._word_list)), str(random.randint(0,9))+ str(random.randint(0,9)), "_"]
            new_path = new_path +  secrets.choice(tkn)

        # self.paths.append(new_path)
        hashed_path = self._generate_hash(new_path)

        self._add_hashPath_to_dict(hashed_path, new_path)