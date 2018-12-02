#! /usr/bin/env python3

count_doubles = 0
count_triplets = 0
with open ('input.txt') as ids:
    for id in ids:
        counts = {}
        for letter in id.strip():
            try:
                counts[letter] += 1
            except KeyError:
                counts[letter] = 1
        found_double = False
        found_triple = False
        for count in counts.values():
            if not found_double and count == 2:
                found_double = True
                count_doubles += 1
            if not found_triple and count == 3:
                found_triple = True
                count_triplets += 1
            if found_double and found_triple:
                break
print("checksum =", count_doubles * count_triplets)     # 5880