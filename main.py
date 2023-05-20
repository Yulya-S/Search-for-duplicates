import os
import time


def crc(data):
    h = 0
    for ki in data:
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = h ^ ki
    return h


def pjw(data):
    h = 0
    for ki in data:
        h = (h << 4) + ki
        g = h & 0xf0000000
        if (g != 0):
            h = h ^ (g >> 24)
            h = h ^ g
    return h


def buz(data):
    h = 0
    R = dict()
    for r, i in enumerate(data):
        R[i] = r
    for ki in data:
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R[ki]
    return h


def _hash(data):
    return hash(data)


def find_duplicates(files: list[str], hash_function: callable) -> list[str]:
    hashes = []
    duplicate_count = 0
    start_time = time.time()
    for i in files:
        with open("out\\" + str(i), "rb") as file:
            text = file.read()
            h = hash_function(text)
            if h not in hashes:
                hashes.append(h)
            else:
                duplicate_count += 1
    print(duplicate_count, time.time() - start_time)


find_duplicates(os.listdir("out"), crc)
find_duplicates(os.listdir("out"), pjw)
find_duplicates(os.listdir("out"), buz)
find_duplicates(os.listdir("out"), _hash)
