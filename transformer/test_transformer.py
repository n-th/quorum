import unittest

from data.models import (Bill, BillResult, Legislator, LegislatorResult, Vote,
                         VoteResult)
from transformer.transformer import Transformer


class TransformerTestCase(unittest.TestCase):
    def setUp(self):
        bills = [
            Bill(1, 'Bill 1', 1),
            Bill(2, 'Bill 2', 2),
            Bill(3, 'Bill 3', 3),
            Bill(4, 'Bill 4', 4),
        ]
        votes = [
            Vote(1, 1),
            Vote(2, 1),
            Vote(3, 2),
            Vote(4, 3),
            Vote(5, 3)
        ]
        legislators = [
            Legislator(1, 'Legislator 1'),
            Legislator(2, 'Legislator 2'),
            Legislator(3, 'Legislator 3')
        ]
        vote_results = [
            VoteResult(1, 1, 1, 1),
            VoteResult(2, 1, 2, 1),
            VoteResult(3, 2, 3, 2),
            VoteResult(4, 2, 4, 2),
            VoteResult(5, 3, 5, 1)
        ]

        self.transformer = Transformer(bills, votes, legislators, vote_results)

    def test_analyze_legislators(self):
        actual_results = self.transformer.analyze_legislators()
        expected_results = [
            LegislatorResult(1, 'Legislator 1', 2, 0),
            LegislatorResult(2, 'Legislator 2', 0, 2),
            LegislatorResult(3, 'Legislator 3', 1, 0)
        ]

        actual_results_sorted = sorted(actual_results, key=lambda x: x.id)
        expected_results_sorted = sorted(expected_results, key=lambda x: x.id)

        self.assertEqual(actual_results_sorted, expected_results_sorted)

    def test_analyze_bills(self):
        expected_results = [
            BillResult(1, 'Bill 1', 2, 0, 'Legislator 1'),
            BillResult(2, 'Bill 2', 0, 1, 'Legislator 2'),
            BillResult(3, 'Bill 3', 1, 1, 'Legislator 3'),
            BillResult(4, 'Bill 4', 0, 0, 'Unknown')
        ]
        actual_results = self.transformer.analyze_bills()

        actual_results_sorted = sorted(actual_results, key=lambda x: x.id)
        expected_results_sorted = sorted(expected_results, key=lambda x: x.id)

        self.assertEqual(actual_results_sorted, expected_results_sorted)

    def test_analyze_data(self):
        expected_legislator_results = [
            LegislatorResult(1, 'Legislator 1', 2, 0),
            LegislatorResult(2, 'Legislator 2', 0, 2),
            LegislatorResult(3, 'Legislator 3', 1, 0)
        ]
        expected_bill_results = [
            BillResult(1, 'Bill 1', 2, 0, 'Legislator 1'),
            BillResult(2, 'Bill 2', 0, 1, 'Legislator 2'),
            BillResult(3, 'Bill 3', 1, 1, 'Legislator 3'),
            BillResult(4, 'Bill 4', 0, 0, 'Unknown')
        ]
        actual_legislator_results, actual_bill_results = self.transformer.analyze_data()

        actual_legislator_results_sorted = sorted(actual_legislator_results, key=lambda x: x.id)
        expected_legislator_results_sorted = sorted(expected_legislator_results, key=lambda x: x.id)

        actual_bill_results_sorted = sorted(actual_bill_results, key=lambda x: x.id)
        expected_bill_results_sorted = sorted(expected_bill_results, key=lambda x: x.id)

        self.assertEqual(actual_legislator_results_sorted, expected_legislator_results_sorted)
        self.assertEqual(actual_bill_results_sorted, expected_bill_results_sorted)

if __name__ == '__main__':
    unittest.main()