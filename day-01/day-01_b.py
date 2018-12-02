#! /usr/bin/env python3

frequency = 0
past_frequencies = set()
duplicate_frequency_found = False

# Continously iterate over the list of changes until a duplicate frequency has been found.
while not duplicate_frequency_found:
    
    # Read file with frequency changes.
    with open('./input.txt') as frequency_changes:
    
        # Iterate over the list of frequency changes.
        for change in frequency_changes:

            # Apply change to frequency.
            frequency += int(change)
            
            # If changed frequency is a duplicate, break out of both loops...
            if frequency in past_frequencies:
                duplicate_frequency_found = True
                break
            
            # otherwise add frequency to the set of past frequencies.
            else:
                past_frequencies.add(frequency)
print("Duplicate frequency:", frequency)