import csv

from data.models import Bill, Legislator, Vote, VoteResult


class Extractor:
    """
    A class for handling data extraction.

    Args:
        folder_path (str): The path to the directory containing the data files.
    """
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_data(self):
        """
        Extracts the data from the CSV files.

        Returns:
            Tuple: A tuple containing the extracted data (bills, votes, legislators, vote_results).
        """
        bills = self.extract_bills()
        votes = self.extract_votes()
        legislators = self.extract_legislators()
        vote_results = self.extract_vote_results()
        return bills, votes, legislators, vote_results

    def extract_bills(self):
        """
        Extracts the bill data from the 'bills.csv' file.

        Returns:
            list: A list of Bill objects representing the extracted bills.
        """
        folder_path = self.folder_path + 'bills.csv'
        return self._extract_csv_data(folder_path, Bill, [int, str, int])

    def extract_votes(self):
        """
        Extracts the vote data from the 'votes.csv' file.

        Returns:
            list: A list of Vote objects representing the extracted votes.
        """
        folder_path = self.folder_path + 'votes.csv'
        return self._extract_csv_data(folder_path, Vote, [int, int])

    def extract_legislators(self):
        """
        Extracts the legislator data from the 'legislators.csv' file.

        Returns:
            list: A list of Legislator objects representing the extracted legislators.
        """
        folder_path = self.folder_path + 'legislators.csv'
        return self._extract_csv_data(folder_path, Legislator, [int, str])

    def extract_vote_results(self):
        """
        Extracts the vote result data from the 'vote_results.csv' file.

        Returns:
            list: A list of VoteResult objects representing the extracted vote results.
        """
        folder_path = self.folder_path + 'vote_results.csv'
        return self._extract_csv_data(folder_path, VoteResult, [int, int, int, int])

    def _extract_csv_data(self, folder_path, model_class, field_types):
        """
        Extracts data from a CSV file and creates instances of the specified model class.

        Args:
            file_path (str): The path to the CSV file.
            model_class (class): The class of the model representing the data.
            field_types (list): A list of field types corresponding to the model's constructor arguments.

        Returns:
            list: A list of model instances representing the extracted data.
        """
        data = []

        with open(folder_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                row_data = [field_type(value) for value, field_type in zip(row, field_types)]
                instance = model_class(*row_data)
                data.append(instance)

        return data
