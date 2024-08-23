import unittest
from app import app, db
from app.models import DNASequence

class TestFullFlow(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_dna_analysis_flow(self):
        response = self.client.post('/', data={'sequence': 'ATCG'})
        self.assertEqual(response.status_code, 302)
        sequence = DNASequence.query.first()
        self.assertIsNotNone(sequence)
        self.assertIn('GC Content', sequence.analysis_result)

    def test_dna_analysis_file_upload(self):
        with open('test_dna.txt', 'w') as f:
            f.write('ATGCGCTAG')
        with open('test_dna.txt', 'rb') as f:
            response = self.client.post('/', data={'file': f})
        self.assertEqual(response.status_code, 302)
        sequence = DNASequence.query.first()
        self.assertIsNotNone(sequence)
        self.assertIn('Start codon', sequence.analysis_result)

if __name__ == '__main__':
    unittest.main()
