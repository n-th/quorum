from extractor.extractor import Extractor
from loader.loader import Loader
from transformer.transformer import Transformer


def main():
    folder_path = './data/'

    extractor = Extractor(folder_path)
    bills, votes, legislators, vote_results = extractor.extract_data()

    transformer = Transformer(bills, votes, legislators, vote_results)
    legislator_results, bill_results = transformer.analyze_data()

    loader = Loader(folder_path)
    loader.write_legislator_results(legislator_results)
    loader.write_bill_results(bill_results)

if __name__ == '__main__':
    main()
