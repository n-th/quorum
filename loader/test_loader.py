import unittest
from io import StringIO
from unittest.mock import patch

from data.models import BillResult, LegislatorResult
from loader.loader import Loader


class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        self.loader = Loader('/path/to/files/')

    def tearDown(self):
        pass

    def test_write_legislator_results(self):
        legislator_results = [
            LegislatorResult('1', 'Legislator 1', 5, 2),
            LegislatorResult('2', 'Legislator 2', 3, 1)
        ]

        expected_csv = '''Legislator ID,Name,Supported Bills,Opposed Bills\r\n1,Legislator 1,5,2\r\n2,Legislator 2,3,1\r\n'''

        with patch('builtins.open', create=True) as mock_open:
            mock_file = StringIO()
            mock_open.return_value.__enter__.return_value = mock_file

            self.loader.write_legislator_results(legislator_results)

            mock_open.assert_called_once_with('/path/to/files/legislators_support_oppose_count.csv', 'w', newline='')

            self.assertEqual(mock_file.getvalue(), expected_csv)

    def test_write_bill_results(self):
        bill_results = [
            BillResult('1', 'Bill 1', 10, 3, 'Legislator 1'),
            BillResult('2', 'Bill 2', 5, 1, 'Legislator 1')
        ]

        expected_csv = '''Bill ID,Title,Supporter Count,Opposed Count,Primary Sponsor\r\n1,Bill 1,10,3,Legislator 1\r\n2,Bill 2,5,1,Legislator 1\r\n'''

        with patch('builtins.open', create=True) as mock_open:
            mock_file = StringIO()
            mock_open.return_value.__enter__.return_value = mock_file

            self.loader.write_bill_results(bill_results)

            mock_open.assert_called_once_with('/path/to/files/bills_title_support_oppose_sponsor_count.csv', 'w', newline='')

            self.assertEqual(mock_file.getvalue(), expected_csv)

if __name__ == '__main__':
    unittest.main()

