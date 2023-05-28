
from data.models import BillResult, LegislatorResult


class Transformer:
    """
    A class for handling data transformation.

    Args:
        bills (list): A list of Bill objects.
        votes (list): A list of Vote objects.
        legislators (list): A list of Legislator objects.
        vote_results (list): A list of VoteResult objects.

    """
    def __init__(self, bills, votes, legislators, vote_results):
        self.bills = bills
        self.votes = votes
        self.legislators = legislators
        self.vote_results = vote_results

    def analyze_legislators(self):
        """
        Analyzes the bills based on the vote results.

        Args:
            legislators (list): A list of Legislator objects.
            vote_results (list): A list of VoteResult objects.

        Returns:
            list: A list of LegislatorResult objects representing the analysis results for each legislator.
        """
        legislator_results = []

        for legislator in self.legislators:
            num_supported_bills = sum(
                1 for vote_result in self.vote_results
                if vote_result.legislator_id == legislator.id and vote_result.vote_type == 1
            )
            num_opposed_bills = sum(
                1 for vote_result in self.vote_results
                if vote_result.legislator_id == legislator.id and vote_result.vote_type == 2
            )

            legislator_result = LegislatorResult(
                legislator.id, 
                legislator.name, 
                num_supported_bills, 
                num_opposed_bills
            )
            legislator_results.append(legislator_result)

        return legislator_results

    def analyze_bills(self):
        """
        Analyzes the bills based on the vote results.

        Args:
            bills (list): A list of Bill objects.
            votes (list): A list of Vote objects.
            legislators (list): A list of Legislator objects.
            vote_results (list): A list of VoteResult objects.

        Returns:
            list: A list of BillResult objects representing the analysis results for each bill.
        """
        bill_results = []

        for bill in self.bills:
            supporter_count = sum(
                1 for vote_result in self.vote_results
                if vote_result.vote_id 
                in [vote.id for vote in self.votes if vote.bill_id == bill.id] 
                and vote_result.vote_type == 1
            )
            opposer_count = sum(
                1 for vote_result in self.vote_results
                if vote_result.vote_id 
                in [vote.id for vote in self.votes if vote.bill_id == bill.id] 
                and vote_result.vote_type == 2
            )

            primary_sponsor = next((legislator.name for legislator in self.legislators if legislator.id == bill.sponsor_id), "Unknown")

            bill_result = BillResult(
                bill.id, 
                bill.title, 
                supporter_count, 
                opposer_count, 
                primary_sponsor
            )
            bill_results.append(bill_result)

        return bill_results

    def analyze_data(self):
        """
        Analyze the data from the CSV files for bills and legislators.

        Returns:
            Tuple: A tuple containing the extracted data (legislator_results, bill_results).
        """
        legislator_results = self.analyze_legislators()
        bill_results = self.analyze_bills()
        return legislator_results, bill_results
