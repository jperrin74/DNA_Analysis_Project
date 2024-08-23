import re

def analyze_dna(sequence):
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence)
    analysis = [f"GC Content: {gc_content:.2%}"]

    # Pattern matching: Example to find a specific gene sequence
    if re.search(r'ATG(?:...)*?(?:TAG|TAA|TGA)', sequence):
        analysis.append("Start codon (ATG) followed by stop codon detected.")
    else:
        analysis.append("No start-stop codon pattern detected.")

    # Mutation detection (simple example): Check for mutations compared to a reference sequence
    reference = "GATTACA"
    mutations = sum(1 for a, b in zip(sequence, reference) if a != b)
    analysis.append(f"Detected {mutations} mutation(s) compared to reference sequence {reference}.")

    return "\n".join(analysis)
