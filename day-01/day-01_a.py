#! /usr/bin/env python3

frequency = 0
with open('./input.txt') as frequencies:
    for freq in frequencies:
        frequency += int(freq)
print("Final frequency:", frequency)