import unittest
from app.forms import DNAForm

class TestForms(unittest.TestCase):
    def test_dna_form_valid(self):
        form = DNAForm(sequence="ATCG")
        self.assertTrue(form.validate())

if __name__ == '__main__':
    unittest.main()
