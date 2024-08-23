from dna_publisher import publish_event

def analyze_dna(sequence):
    # Perform DNA analysis here
    result = "No start codon found"  # Example result
    message = f"Analysis complete for sequence {sequence}: {result}"
    
    # Publish event after analysis
    publish_event(message)

    return result

if __name__ == "__main__":
    dna_sequence = "ATTGAGATCATA"
    analyze_dna(dna_sequence)
