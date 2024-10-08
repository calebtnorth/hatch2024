# Find variations within a genomic FASTA file
from os.path import isfile
from re import search
from subprocess import Popen, PIPE

class FASTA:

    def __init__(self, data:str):
        data_by_line = data.split("\n")
        self.sequence = "".join(data_by_line[1:]).strip()

        regex_identifer = "[A-Z]{2}_\d+.\d+"
        regex_match = search(regex_identifer, data_by_line[0])
        if not regex_match:
            raise ValueError(f"No ID found in FASTA file")
        self.id = regex_match.group()

        if "MTHFR" in data_by_line[0]:
            self.ref_type = "MTHFR"

    @staticmethod
    def find_variant(seqs:list["FASTA"], search_sensitivity:int=16) -> list[str]:
        # Render all sequences into one
        sumseq = ""
        for seq in seqs:
            sumseq += f">{seq.id}\n{seq.sequence}\n"

        # clustalout for stars
        process = Popen(["mafft", "--quiet", "--auto", "-"], stdin=PIPE, stdout=PIPE)
        process.stdin.write(sumseq.encode())

        process_stdout = process.communicate()[0].decode("utf8")
        aligned_fastas = []
        for split_process_stdout in process_stdout.split(">"):
            if split_process_stdout == "":
                continue
            aligned_fastas.append(
                FASTA(split_process_stdout)
            )
        with open("./temp.txt", "w+") as file:
            file.write("".join([f.sequence+"\n" for f in aligned_fastas]))
        process.stdin.close()

        # Buffer one backwards and set everything to sequences
        ref_fasta = aligned_fastas[0].sequence
        aligned_seq = [fasta.sequence for fasta in aligned_fastas[1:]]

        for letter_index in range(search_sensitivity, len(ref_fasta) - search_sensitivity):
            letter_index_score = 0
            for fasta in aligned_seq:
                # Make sure it's not blank
                if fasta[letter_index] == "-":
                    continue
                # Matching letter? Skip
                if fasta[letter_index] == ref_fasta[letter_index]:
                    continue

                # Check padding
                if fasta[letter_index - search_sensitivity:letter_index] != ref_fasta[letter_index - search_sensitivity:letter_index] or \
                    fasta[letter_index + 1:letter_index + search_sensitivity] != ref_fasta[letter_index + 1:letter_index + search_sensitivity]:
                        continue
                # A single difference found! Return index
                return [fasta.sequence[letter_index] for fasta in aligned_fastas]
        return []

class FASTAFile(FASTA):
    # Cache filepath on creation
    def __init__(self, filepath:str):
        if not isfile(filepath):
            raise FileNotFoundError(f"No such file at path {filepath}")
        # Divide the file by linebreak
        with open(filepath, "r") as file:
            super().__init__(file.read())
