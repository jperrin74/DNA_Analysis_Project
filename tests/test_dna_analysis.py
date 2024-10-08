import unittest
import sys
import os

# Adjust sys.path to include the root of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import app, db
from app.models import DNASequence

class DNATestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'DNA Analysis', response.data)

    def test_dna_analysis(self):
        dna = DNASequence(sequence='ATCG')
        db.session.add(dna)
        db.session.commit()

        retrieved = DNASequence.query.first()
        self.assertEqual(retrieved.sequence, 'ATCG')

if __name__ == '__main__':
    unittest.main()
