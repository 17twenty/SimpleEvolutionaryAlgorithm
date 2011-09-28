#!/usr/bin/env python

import random
import string
import time

source = "jiKnp4bsdfasdfasdf32423edsfdfgdasdf!fdsasdfa\dqpmAbp"
target = "It was the best of times, it was the worst of times."

def calc_fitness(source, target):
    fitval = 0
    for i in range(0, len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return(fitval)

def mutate(parent1, parent2):
   child_dna = parent1['dna'][:]

   # Mix both DNAs
   start = random.randint(0, len(parent2['dna']) - 1)
   stop = random.randint(0, len(parent2['dna']) - 1)
   if start > stop:
      stop, start = start, stop
   child_dna[start:stop] = parent2['dna'][start:stop]

   # Mutate one position
   charpos = random.randint(0, len(child_dna) - 1)
   child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
   child_fitness = calc_fitness(child_dna, target)
   return({'dna': child_dna, 'fitness': child_fitness})
   
def random_parent(genepool):
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    wRndNr = int(wRndNr)
    return(genepool[wRndNr])

print "Started..."
GENSIZE = 20
genepool = []
for i in range(0, GENSIZE):
    dna = [random.choice(string.printable[:-5]) for j in range(0, len(target))]
    fitness = calc_fitness(dna, target)
    candidate = {'dna': dna, 'fitness': fitness }
    genepool.append(candidate)
    
while True:
    genepool.sort(key=lambda candidate: candidate['fitness'])

    # Check if we're fit enough
    if genepool[0]['fitness'] == 0:
        break

    parent1 = random_parent(genepool)
    parent2 = random_parent(genepool)
    child = mutate(parent1, parent2)
    
    p1 = "".join(parent1['dna'])
    p2 = "".join(parent2['dna'])
    c1 = "".join(child['dna'])
    print "Parent1:  " + p1 + ", Parent2: " + p2 + " -> " + c1 + ", fitness: " + str(child['fitness'])

    if child['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = child
    time.sleep(0.0005)