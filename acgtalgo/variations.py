# Find variations within a genomic FASTA file
from os.path import isfile
from re import search
from subprocess import Popen, PIPE

class FASTA:

    def __init__(self, data):
        data_by_line = data.split("\n")

        # Extract ID
        regex_identifer = "[A-Z]{2}_\d+.\d+"
        regex_match = search(regex_identifer, data_by_line[0])

        if not regex_match:
            raise ValueError(f"No ID found in FASTA file")
        self.id = regex_match.group()

        # Extract sequences
        self.sequence = "".join(data_by_line[1:]).strip() 

    @staticmethod
    def find_variant(seqs:list["FASTA"]) -> int:
        # Render all sequences into one
        sumseq = ""
        for seq in seqs:
            sumseq += f">{seq.id}\n{seq.sequence}\n"

        # clustalout for stars
        process = Popen(["mafft", "--quiet", "-"], stdin=PIPE, stdout=PIPE)
        process.stdin.write(sumseq.encode())

        process_stdout = process.communicate()[0].decode("utf8")
        aligned_fastas = []
        for split_process_stdout in process_stdout.split(">"):
            if split_process_stdout == "":
                continue
            aligned_fastas.append(
                FASTA(split_process_stdout)
            )
        process.stdin.close()

        # Buffer one backwards and set everything to sequences
        ref_fasta = aligned_fastas[0].sequence
        aligned_fastas = [fasta.sequence for fasta in aligned_fastas[1:]]

        for letter_index in range(0, len(ref_fasta) - 1):
            for fasta in aligned_fastas:
                # Match
                if fasta[letter_index] == ref_fasta[letter_index]:
                    continue
                # Two differences in a row means that is not a single alteration. Continue
                if fasta[letter_index + 1] != ref_fasta[letter_index + 1]:
                    continue
                # A single difference found! Return index
                return letter_index

class FASTAFile(FASTA):
    # Cache filepath on creation
    def __init__(self, filepath:str):
        if not isfile(filepath):
            raise FileNotFoundError(f"No such file at path {filepath}")
        # Divide the file by linebreak
        with open(filepath, "r") as file:
            super().__init__(file.read())       