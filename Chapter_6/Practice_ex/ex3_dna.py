# ECOO '12 R1 P2 - Decoding DNA
# https://dmoj.ca/problem/ecoo12r1p2

#  Adenine and Thymine  (A - T) 
#  Cytosine and Guanine (C - G)

# Promoter = Begins 10 bases before the start of the TU > (TATAAT)

# Transcription Unit (TU)

# Terminator = two distinct, complementary, reversed sequences 
#of at least length 6.

# ie input = AGATTA_TATAAT_GATA*GGATTTAGATTGACCC*_GTCATGCA_AGTCCA_TGCATGAC_AGC
# Input Test: 'AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC'

# Output = Complementary to the TU, except that in RNA
# Uracil takes the place of Thymine. (U - T) 

# ie input =  GGATTTAGATTGACCC
# ie output = CCUAAAUCUAACUGGG



def check_promoter(strand: str) -> int:
   
    start = strand.find('TATAAT')
    return start
    
def get_newStrand(strand):
    
    new_strand = strand[(promoter+10):]
    return new_strand

def get_pattern(new_strand):
    
    pattern = new_strand[:6]     
    return pattern
    
def transform_pattern(pattern):
    
    pattern2 = ''
    pattern = pattern[::-1]
    
    for letter in pattern:     #AT CG   
            if letter == 'A':
                pattern2 = pattern2 +'T'
            elif letter == 'T':
                pattern2 = pattern2 +'A'
            elif letter == 'C':
                pattern2 = pattern2 +'G'
            else:
                pattern2 = pattern2 +'C'
    return pattern2

def is_occurrence(strand, pattern2, index, pattern)-> int:
    
    occurrence = strand.find(pattern2)
    return occurrence
    

def check_terminator(strand: str, promoter: int):

    index = -1
    new_strand = get_newStrand(strand)
    while index == -1:
        pattern = get_pattern(new_strand)
        pattern2 = transform_pattern(pattern)
        search_strand = strand[32+(len(pattern)):]
        index = strand.find(pattern)
        occurrence = is_occurrence(search_strand, pattern2, index, pattern)
        if occurrence != -1:
            index = strand.find(pattern)
        else:
            index = -1
            new_strand= new_strand[1:]
    return index, pattern, occurrence

def get_extension(strand, pattern, index):
    end = len(pattern)
    pattern = strand[index:index+end+1]
    return pattern

def check_tu(strand: str, promoter: int, index: int):
    
    trans_unit = strand[(promoter+10):index]
    return trans_unit
    
def get_final_rna(trans_unit):
    
    rna = ''
    for letter in trans_unit:     #AT CG CCUAAAUCUAACUGGG
                                         
            if letter == 'A':
                rna = rna +'U'
            elif letter == 'T':
                rna = rna +'A'
            elif letter == 'C':
                rna = rna +'G'
            else:
                rna = rna +'C'
    return rna





# Main //////////////////////////////////////////////////////////////////////////////////////////////////

# Read input..............................................OK
strands = []
rnas = []

ocurrence = 0
for n in range(3):
    strands.append(str(input()))

for strand in strands:
    # Find promoter.......................................OK
    promoter = check_promoter(strand)

    # Find Terminator.....................................OK
    index, pattern, occurrence = check_terminator(strand, promoter)

    # Check extension.....................................TODO
    last_pattern_ok = pattern
    while occurrence != -1:
        pattern = get_extension(strand, pattern, index)
        pattern2 = transform_pattern(pattern)
        occurrence = is_occurrence(strand, pattern2, index, pattern)
    last_pattern_ok = pattern
    
    # Find TU.............................................OK
    trans_unit = check_tu(strand, promoter, index)
    rna = get_final_rna(trans_unit)
    rnas.append(rna)
    rna = ''


for s in range(1,len(rnas)+1):
    print(f'{s}: {rnas[s-1]}')