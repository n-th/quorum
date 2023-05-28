class Vote:
    """
    Represents a vote.
    """
    def __init__(self, id: int, bill_id: int):
        """
        Initialize a Vote instance.

        Args:
            id (int): The ID of the vote.
            bill_id (int): The ID of the associated bill.
        """
        self.id = id
        self.bill_id = bill_id

    def __eq__(self, other):
        if isinstance(other, Vote):
            return self.id == other.id and self.bill_id == other.bill_id
        return False

class Legislator:
    """
    Represents a legislator.
    """
    def __init__(self, id: int, name: str):
        """
        Initialize a Legislator instance.

        Args:
            id (int): The ID of the legislator.
            name (str): The name of the legislator.
        """
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Legislator):
            return self.id == other.id and self.name == other.name
        return False

class LegislatorResult:
    """
    Represents the result of a legislator's analysis.
    """
    def __init__(self, id: int, name: str, num_supported_bills: int, num_opposed_bills: int):
        """
        Initialize a LegislatorResult instance.

        Args:
            id (int): The ID of the legislator.
            name (str): The name of the legislator.
            num_supported_bills (int): The number of bills supported by the legislator.
            num_opposed_bills (int): The number of bills opposed by the legislator.
        """
        self.id = id
        self.name = name
        self.num_supported_bills = num_supported_bills
        self.num_opposed_bills = num_opposed_bills

    def __str__(self):
        return (
            f"Legislator ID: {self.id}," 
            f"Name: {self.name}, "
            f"Supported Bills: {self.num_supported_bills}, "
            f"Opposed Bills: {self.num_opposed_bills}"
        )
    
    def __eq__(self, other):
        if isinstance(other, LegislatorResult):
            return (
                self.id == other.id 
                and self.name == other.name 
                and self.num_opposed_bills == other.num_opposed_bills 
                and self.num_supported_bills ==  other.num_supported_bills
            )
        return False


class BillResult:
    """
    Represents the result of a bill's analysis.
    """
    def __init__(self, id: int, title: str, supporter_count: int, opposer_count: int, primary_sponsor: str):
        """
        Initialize a BillResult instance.

        Args:
            id (int): The ID of the bill.
            title (str): The title of the bill.
            supporter_count (int): The number of legislators supporting the bill.
            opposer_count (int): The number of legislators opposing the bill.
            primary_sponsor (str): The name of the primary sponsor of the bill.
        """
        self.id = id
        self.title = title
        self.supporter_count = supporter_count
        self.opposer_count = opposer_count
        self.primary_sponsor = primary_sponsor

    def __eq__(self, other):
        if isinstance(other, BillResult):
            return (
                self.id == other.id 
                and self.title == other.title 
                and self.supporter_count == other.supporter_count 
                and self.opposer_count == other.opposer_count 
                and self.primary_sponsor == other.primary_sponsor
            )
        return False

    def __str__(self):
        return (
            f"Bill ID: {self.id}, "
            f"Title: {self.title}, "
            f"Supporter Count: {self.supporter_count}, Opposed Count: {self.opposer_count}, "
            f"Sponsor_id: {self.primary_sponsor}"
        )


class VoteResult:
    """
    Represents the result of a vote.
    """
    def __init__(self, id: int, legislator_id: int, vote_id: int, vote_type: int):
        """
        Initialize a VoteResult instance.

        Args:
            id (int): The ID of the vote result.
            legislator_id (int): The ID of the legislator associated with the vote.
            vote_id (int): The ID of the vote.
            vote_type (int): The type of the vote (1 for support, 2 for opposition).
        """
        self.id = id
        self.legislator_id = legislator_id
        self.vote_id = vote_id
        self.vote_type = vote_type


    def __eq__(self, other):
        if isinstance(other, VoteResult):
            return (
                self.id == other.id 
                and self.legislator_id == other.legislator_id 
                and self.vote_id == other.vote_id 
                and self.vote_type == other.vote_type
            )
        return False

class Bill:
    """
    Represents a bill.
    """
    def __init__(self, id: int, title: str, sponsor_id: int):
        """
        Args:
            id (int): The ID of the legislator.
            title (str): The name of the bill.
            sponsor_id (int): The name of the legislator.
        """
        self.id = id
        self.title = title
        self.sponsor_id = sponsor_id

    def __eq__(self, other):
        if isinstance(other, Bill):
            return (
                self.id == other.id 
                and self.title == other.title 
                and self.sponsor_id == other.sponsor_id
            )
        return False
