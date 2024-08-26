import re
from typing import List, Tuple

def read_fasta(file_path: str, max_sequences: int = None) -> List[Tuple[str, str]]:
    sequences = []
    current_id = ""
    current_seq = []

    with open(file_path, 'r') as file:
        for line in file:
            if max_sequences and len(sequences) >= max_sequences:
                break
            
            line = line.strip()
            if line.startswith('>'):
                if current_id and current_seq:
                    sequences.append((current_id, ''.join(current_seq)))
                current_id = line[1:].split()[0]  # Extract just the ID
                current_seq = []
            else:
                current_seq.append(line)

    if current_id and current_seq and (not max_sequences or len(sequences) < max_sequences):
        sequences.append((current_id, ''.join(current_seq)))

    return sequences

def clean_sequence(sequence: str) -> str:
    # Remove any non-amino acid characters
    return re.sub(r'[^ACDEFGHIKLMNPQRSTVWY]', '', sequence.upper())

def preprocess_fasta(input_file: str, output_file: str, max_sequences: int = None):
    sequences = read_fasta(input_file, max_sequences)
    
    with open(output_file, 'w') as out_file:
        for seq_id, seq in sequences:
            cleaned_seq = clean_sequence(seq)
            if cleaned_seq:  # Only write non-empty sequences
                out_file.write(f">{seq_id}\n{cleaned_seq}\n")

if __name__ == "__main__":
    input_file = "data/uniparc_tiny_subset.fasta"
    output_file = "data/cleaned_data/cleaned_uniparc_tiny_subset.fasta"
    max_sequences = 100  # Process only 100 sequences
    preprocess_fasta(input_file, output_file, max_sequences)
    print(f"Preprocessed {max_sequences} sequences saved to {output_file}")