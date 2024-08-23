import unittest
from app import app, db
from app.models import DNASequence

class TestModels(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_dna_sequence_model(self):
        sequence = DNASequence(sequence="ATCG", analysis_result="GC Content: 50%")
        db.session.add(sequence)
        db.session.commit()
        self.assertEqual(sequence.sequence, "ATCG")

if __name__ == '__main__':
    unittest.main()
