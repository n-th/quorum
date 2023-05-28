import csv


class Loader:
    """
    A class for handling data loading.

    Args:
        folder_path (str): The path to the directory that will contain the resulting data files.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def write_legislator_results(self, legislator_results):
        """
        Write the legislator resulting data into the CSV files.
        """
        file_path = self.file_path + 'legislators_support_oppose_count.csv'
        fieldnames = ['Legislator ID', 'Name', 'Supported Bills', 'Opposed Bills']

        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for result in legislator_results:
                writer.writerow({
                    'Legislator ID': result.id,
                    'Name': result.name,
                    'Supported Bills': result.num_supported_bills,
                    'Opposed Bills': result.num_opposed_bills
                })

    def write_bill_results(self, bill_results):
        """
        Write the bill resulting data into the CSV files.
        """
        file_path = self.file_path + 'bills_title_support_oppose_sponsor_count.csv'
        fieldnames = ['Bill ID', 'Title', 'Supporter Count', 'Opposed Count', 'Primary Sponsor']

        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for result in bill_results:
                writer.writerow({
                    'Bill ID': result.id,
                    'Title': result.title,
                    'Supporter Count': result.supporter_count,
                    'Opposed Count': result.opposer_count,
                    'Primary Sponsor': result.primary_sponsor
                })
