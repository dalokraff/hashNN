from hashing.hasher import HashDict
from tqdm import tqdm

hashinary = HashDict("words.txt")

iterations = int(input("Number of hashes to generate?\t"))
print("Generating hashes. . .")
for i in tqdm(range(iterations)):
    hashinary.generate_new_path()

print("Writing hashes to file...")
f = open("hashes.txt", "a")
for hash,name in hashinary.hashPath_dict.items():  
    f.write(f'{hash}\t{name}\n')
f.close()
print("Hashes written to file!")