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
import matplotlib.pyplot as plt


with open('files\dna.fasta', 'r') as dna_file:
    dna_lines = dna_file.readlines()
    dna = []
    dna_names = []
    for line in dna_lines:
        if line.startswith('>'):
            dna.append('')
            dna_names.append(line[1:].strip())
            continue
        dna[-1] += line.strip()

     
with open(r'files\rna_codon_table.txt', 'r') as codon_table_file:
    codon_table = codon_table_file.read()


codon_table = codon_table.split()
codon_dict = {codon_table[i]:codon_table[i+1] for i in range(0, len(codon_table), 2)}


def translate_from_dna_to_rna(dna):
    """Returns list of RNA genes from list of DNA genes"""

    rna = []
    for gene in dna:
        rna.append(gene.replace('T', 'U'))
    return rna


def count_nucleotides(dna):
    """Returns statistics of A, C, G, T nucleotides in DNA

    Takes list of DNA genes and returns list of dicts with stats"""
    num_of_nucleotides = []
    for gene in dna:
        num_of_nucleotides.append({'A':gene.count('A'), 'C':gene.count('C'),
                                   'G':gene.count('G'), 'T':gene.count('T')})
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    """Returns list of proteins from list of RNA"""
    
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


def dna_transcription_file_output(dna):
    """Writes 3 files:
    1. Nucleotides statistics in DNA
    2. RNA list from DNA
    3. Proteins from RNA using codon_table"""

    nucleotides_stats = count_nucleotides(dna)
    rna = translate_from_dna_to_rna(dna)
    protein = translate_rna_to_protein(rna)

    with open('nucleotides_stats.txt', 'w') as nuc_file:
        nuc_file.write(str(nucleotides_stats))
    with open('rna.txt', 'w') as rna_file:
        rna_file.write(str(rna))
    with open('protein_codons.txt', 'w') as protein_file:
        protein_file.write(str(protein))

    # draw hist
    gene_1 = plt.bar(nucleotides_stats[0].keys(), nucleotides_stats[0].values(),
                     width = 0.4, align = 'edge', label = dna_names[0])
    gene_2 = plt.bar(nucleotides_stats[1].keys(), nucleotides_stats[1].values(),
                     width = 0.4, align = 'center', label = dna_names[1])

    plt.xlabel('Nucleotides name')
    plt.ylabel('Nucleotides count')
    for rect in gene_1 + gene_2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=1, borderaxespad=0.)

    plt.savefig('nucleotides_stats_hist.png')

dna_transcription_file_output(dna)
