# Generate chemical differences because of genetic changes

from requests import post, get
from variations import FASTA, FASTAFile

COMPOUNDS:dict = {
    "MTHFR":    {
        "chemical": "folate",
        "average": 400,
        "kgunit": 10e-7,
        "variations": {
            "cc": 1.0,
            "ct": .65,
            "tt": .15
        }
    }
}

def generate_chemical_weight(fasta_paths:list[str], type:str) -> float:
    chemical_score:int = 1
    fastas:list = [FASTAFile(path) for path in fasta_paths]
    variants = FASTA.find_variant(fastas)
    
    # No variations. Normal diet
    if not variants:
        return -1.0
    
    # Weight variations. Assume double
    for letter in variants:
        chemical_score += float(COMPOUNDS[type.upper()]["variations"][letter*2])
    return 1.0 / (chemical_score / len(variants))





