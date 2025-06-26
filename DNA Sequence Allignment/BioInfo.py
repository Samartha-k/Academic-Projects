def needleman_wunsch(seq1, seq2):
    match = 1
    mismatch = -1
    gap = -2
    matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    for i in range(len(seq1) + 1):
        matrix[i][0] = i * gap
    for j in range(len(seq2) + 1):
        matrix[0][j] = j * gap
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score = match
            else:
                score = mismatch
            diagonal = matrix[i - 1][j - 1] + score
            up = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap
            matrix[i][j] = max(diagonal, up, left)
    alignment_seq1 = ""
    alignment_seq2 = ""
    i = len(seq1)
    j = len(seq2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (
        match if seq1[i - 1] == seq2[j - 1] else mismatch):
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = "-" + alignment_seq2
            i -= 1
        else:
            alignment_seq1 = "-" + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            j -= 1
    sequences_match = alignment_seq1 == alignment_seq2
    return alignment_seq1, alignment_seq2, sequences_match
sequence1 = "AATCG"
sequence2 = "AACG"
alignment1, alignment2, sequences_match = needleman_wunsch(sequence1, sequence2)
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)
