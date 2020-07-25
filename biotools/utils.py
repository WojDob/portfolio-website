import numpy as np

def count_words(seq, word_size):
    """Count subsequences (k-mers) in seq of given length
    """
    d = {}
    for i in range(0, len(seq)-word_size+1):
        word = seq[i:i+word_size]
        if word not in d:
            d[word] = 0
        d[word] += 1
    n = sum(d.values())
    for word in d:
        d[word] = [d[word], d[word] / n * 100]
    return d

def chooseMethod(seq,method):
    cleanSeq = removeFastaID(seq)
    if method == "reverseComplement":
        return addNewLines(reverseComplementarySequence(cleanSeq))
    elif method == "reverse":
        return addNewLines(reverseSequence(cleanSeq))
    elif method == "complement":
        return addNewLines(complementarySequence(cleanSeq))
    else:
        return "something bad happened"

def removeFastaID(seq):
    if seq[0]=='>':
        return '\n'.join(seq.split('\n')[1:])
    return seq

def addNewLines(seq):
    newSeqList = list()
    for nucNumber in range (len(seq)):
        if nucNumber % 60 == 0:
            newSeqList.append('<br />')
        newSeqList.append(seq[nucNumber])
    return ''.join(newSeqList)

def reverseComplementarySequence(seq):
    return ''.join(reverseSequence(complementarySequence(seq)))

def reverseSequence(seq):
    return seq[::-1]

def complementarySequence(seq):
    complementary = {'A':'T','T':'A','G':'C','C':'G'}
    return ''.join([complementary[x] if x in complementary else x for x in seq ])

def generateRandomDNA(length,propabilities):
    BASES = ('A', 'C', 'G', 'T')
    return addNewLines(''.join(np.random.choice(BASES, p=propabilities) for _ in range(length)))

