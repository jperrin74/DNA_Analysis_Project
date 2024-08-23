import unittest
from app.analyzer import analyze_dna

class TestAnalyzer(unittest.TestCase):
    def test_analyze_dna_gc_content(self):
        sequence = "GCGCGC"
        result = analyze_dna(sequence)
        self.assertIn("GC Content: 100.00%", result)

    def test_analyze_dna_pattern_matching(self):
        sequence = "ATGGGGTAG"
        result = analyze_dna(sequence)
        self.assertIn("Start codon (ATG) followed by stop codon detected.", result)

    def test_analyze_dna_mutation_detection(self):
        sequence = "GATTTCA"
        result = analyze_dna(sequence)
        self.assertIn("Detected 1 mutation(s) compared to reference sequence GATTACA.", result)

if __name__ == '__main__':
    unittest.main()
