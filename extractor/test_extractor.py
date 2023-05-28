import unittest
from unittest.mock import patch

from data.models import Bill, Legislator, Vote, VoteResult
from extractor.extractor import Extractor


class ExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor('/path/to/files/')

    def test_extract_bills(self):
        sample_data = [
            'id,title,sponsor_id\n',
            '1,Bill 1,100\n',
            '2,Bill 2,50\n',
            '3,Bill 3,75\n'
        ]

        expected_results = [
            Bill(1, 'Bill 1', 100),
            Bill(2, 'Bill 2', 50),
            Bill(3, 'Bill 3', 75)
        ]

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.__iter__.return_value = sample_data

            actual_results = self.extractor.extract_bills()

            mock_open.assert_called_once_with(self.extractor.folder_path + 'bills.csv', 'r')

            self.assertListEqual(actual_results, expected_results)


    def test_extract_votes(self):
        sample_data = [
            'id,bill_id\n',
            '1,101\n',
            '2,102\n',
            '3,103\n'
        ]
        expected_results = [
            Vote(1, 101),
            Vote(2, 102),
            Vote(3, 103)
        ]

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.__iter__.return_value = sample_data

            actual_results = self.extractor.extract_votes()

            mock_open.assert_called_once_with(self.extractor.folder_path + 'votes.csv', 'r')
            self.assertEqual(actual_results, expected_results)

    def test_extract_vote_results(self):
        sample_data = [
            'id,legislator_id,vote_id,vote_type\n',
            '1,101,1,2\n',
            '2,102,1,0\n',
            '3,103,0,1\n'
        ]
        expected_results = [
            VoteResult(1, 101, 1, 2),
            VoteResult(2, 102, 1, 0),
            VoteResult(3, 103, 0, 1)
        ]

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.__iter__.return_value = sample_data

            actual_results = self.extractor.extract_vote_results()

            mock_open.assert_called_once_with(self.extractor.folder_path + 'vote_results.csv', 'r')
            self.assertEqual(actual_results, expected_results)

    def test_extract_legislators(self):
        sample_data = [
            'id,name\n',
            '101,John Doe\n',
            '102,Jane Smith\n',
            '103,Michael Johnson\n'
        ]
        expected_results = [
            Legislator(101, 'John Doe'),
            Legislator(102, 'Jane Smith'),
            Legislator(103, 'Michael Johnson')
        ]

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.__iter__.return_value = sample_data

            actual_results = self.extractor.extract_legislators()

            mock_open.assert_called_once_with(self.extractor.folder_path + 'legislators.csv', 'r')
            self.assertEqual(actual_results, expected_results)

if __name__ == '__main__':
    unittest.main()
