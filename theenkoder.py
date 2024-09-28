import random
import string

def keygen():
    key = ((str(random.randint(128, 512) + random.randint(128, 512)) + random.choice(
        string.ascii_letters) + random.choice(string.ascii_letters)
            + str(random.randint(128, 512) + random.randint(128, 512) + random.randint(128, 512))) +
           random.choice(string.ascii_letters) + str(random.randint(128, 512) + random.randint(128, 512))
           + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) +
           str(random.randint(128, 512) + random.randint(128, 512)))

    with open("key.txt", "w") as file:
        file.write(text)


print("")
