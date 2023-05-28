# Quorum Coding Challenge
This is a analysis of legislative data following the instructions on the docs/challenge.pdf. To run this project you will need:

- Python 3.11
- [Python Virtual Env](https://docs.python.org/3/library/venv.html)

## Instructions to run the project

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 main.py
```

The outputs will be located in the data folder, under the names `legislators_support_oppose_count.csv` and `bills_title_support_oppose_sponsor.csv`.

## Explanation

This project is made with three steps. The extracting step where I extract the data from the data/*.csv files, this data is extracted into Bill, Legislator, Vote and Vote Result models.

After the data is extracted, it will go to the transformation part of the process, where we want to answer two questions:

1. For every legislator in the dataset,how many bills did the legislator support (voted for the bill)? How many bills did the legislator oppose?
2. For every bill in the dataset, how many legislators supported the bill? How many legislators opposed the bill? Who was the primary sponsor of the bill?

After the data aggregation, the next goal is to save the outputs using the loader step.

## Answers

1. Discuss your solution’s time complexity. What trade offs did you make?

Let's discuss the time complexity of each module:

- Data Extraction: The time complexity of extracting data from CSV files using the csv module is typically O(n), where n is the number of rows in the CSV file. For each row, the fields are read and processed to create instances of the corresponding model class. This operation iterates through the rows of the CSV file, resulting in a linear time complexity.

- Data Transformation: The time complexity of the data transformation operations depends on the size of the input data. The analyze_legislators and analyze_bills methods iterate over the input lists and perform some calculations based on the vote results. The time complexity of these operations is O(m), where m is the number of vote results.

- Data Loading: The time complexity of loading data into CSV files using the csv module is typically O(k), where k is the number of elements to be written. The write_legislator_results and write_bill_results methods iterate over the input lists and write the data to the corresponding CSV files.

2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?

Lets discuss the change per module:

- Data Extraction: We need to modify the extract_bills method in the Extractor class to extract additional fields, such as "Bill Voted On Date" or "Co-Sponsors," from the CSV file.
Update the Bill model class to include the new fields and modify the __init__ method accordingly.

- Data Transformation: We would update the transformation methods, such as analyze_legislators and analyze_bills, to consider the new columns if they are present in the input data. Modify the LegislatorResult and BillResult classes to include the new fields and update the calculations and aggregations accordingly.

- Data Loading: We can adjust the write_legislator_results and write_bill_results methods in the Loader class to handle the new columns when writing data to the CSV files. We also need to modify the fieldnames and DictWriter instances to include the new column names.

    Regarding the tests, we would need to update them with the new fields and expected results. In the __str__ of each model, we would need to update the checks between self and other, to make sure the address of each model won't be validated by the AssertEqual unittest functions.

3. How would you change your solution if instead of receiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?

    I would make a variation of _extract_csv_data as _extract_list_data, with the new list of legislator or bills, it this question is about the input format of the legislators or bills. Assuming we would have the same data, but in a list of objects, there shouldn't be many changes.

    If the question is regarding passing a list of ids of legislators or ids of bills, and we need to create the output just for those ids, I would change the data transformation class to filter the ids inputed.

    We would need to update the tests as well, to reflect both of changes.

4. How long did you spend working on the assignment?

    Around 3 hours and 12 minutes. It took me a while to write the docstring, the answers and tests for the loader mock.


### My Takes on the Evaluation Criteria

1. Correctness - Is your output correct based on the provided data? How did you prove correctness?

I added unit tests to check correctness of my code. You can check with the following commands:
```bash
python3 -m unittest -v
```
```bash
coverage run -m unittest discover .
covarage report
```

You can also run `coverage html` to get a better visualization.
I am not a fan of defining a percentage goal of coverage, because it is easy to create unuseful tests in order for the pipeline to pass. So I made tests for the most significants functions and feature, and got a 94% coverage.

2. Structure/Readability - Is your code well organized and easy to read? Can it be extended reasonably if new requirements are given?

I believe my code is well organized and easy to read, as the function and variables have easy to understand names, I also took and extra time to add documentation string for classes and functions, not because they were needed but as a way reminder of what the arguments represents. About extending the code reasonably, I made a modular maintanable code, with encapsulations for each step of the data handling pipeline.

3. Proficiency with Language - Does your code make use of typical conventions in your language of choice?

Yes, I followed typical Python conventions that follows the PEP 8 style guidelines, the code is structured into classes and methods, in an OOP principle. I didn't add any style guidelines in the repository but I have used my own vscode style configuration. Overall, I believe my code could be improved with logging and error handling. I also didn't use the Person model that was mentioned in the overview of the code instructions, since we had only legislators and I wasn't sure if we should consider a non legislator.
