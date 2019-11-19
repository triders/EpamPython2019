""""
Задание 1
0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)
1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])
2) Перевод последовательности ДНК в РНК (окей, Гугл)
3) Перевод последовательности РНК в протеин*
*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.
Вход: файл dna.fasta с n-количеством генов
Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена
 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)
P.S. За незакрытый файловый дескриптор - караем штрафным дезе.
"""

gene_num = -1
dna = []
with open(r'files\dna.fasta', 'r') as dna_file:
    dna_lines = dna_file.readlines()
    for line in dna_lines:
        if line[0] == '>':
            gene_num += 1
            dna.append('')
            continue
        dna[gene_num] += line[:-2]
     
with open(r'files\rna_codon_table.txt', 'r') as codon_table_file:
    codon_table = codon_table_file.read()
    for i in codon_table:
        i = i.strip()

codon_table = codon_table.split()
codon_dict = {codon_table[i]:codon_table[i+1] for i in range(0,len(codon_table),2)}


def translate_from_dna_to_rna(dna):
    
    dna_to_rna = {'T': 'A', 'A': 'U', 'C': 'G', 'G': 'C'}
    rna = ['' for i in range(len(dna))]

    gene_num = -1
    for gene in dna:
        gene_num += 1
        for nuc in gene:
            rna[gene_num] += dna_to_rna.get(nuc)
    return rna


def count_nucleotides(dna):

    num_of_nucleotides = []
    for gene in dna:
        num_of_nucleotides.append({'A':gene.count('A'), 'C':gene.count('C'),
                                   'G':gene.count('G'), 'T':gene.count('T')})
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    
    protein = []
    for gene in rna:
        tmp = ''
        for i in range(0, len(gene), 3):
            nuc = gene[i:i+3]
            codon = codon_dict.get(nuc)
            if codon == 'Stop':
                break
            tmp += codon
        protein.append(tmp)
    return protein


#print(count_nucleotides(dna))

#rna = translate_from_dna_to_rna(dna)

#print(translate_rna_to_protein(rna))

def dna_to_protein_file_output(dna):
    nucleotides_stats = count_nucleotides(dna)
    
    rna = translate_from_dna_to_rna(dna)
    protein = translate_rna_to_protein(rna)

    with open(r'nucleotides_stats.txt', 'w') as nuc_file:
        nuc_file.write(str(nucleotides_stats))
    with open(r'rna.txt', 'w') as rna_file:
        rna_file.write(str(rna))
    with open(r'protein_codons.txt', 'w') as protein_file:
        protein_file.write(str(protein))

dna_to_protein_file_output(dna)
