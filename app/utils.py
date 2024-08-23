def analyze_sequence(sequence):
    analysis_result = []
    # Calculate GC Content
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    analysis_result.append(f'GC Content: {gc_content:.2f}%')

    # Check for Start Codon
    def analyze_sequence(sequence):
    # Perform analysis on the sequence
        if 'ATG' in sequence:
            return "Start codon found"
    return "No start codon found"


