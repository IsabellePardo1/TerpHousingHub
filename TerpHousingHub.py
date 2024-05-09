""" 
This script allows for UMD students to browse through student housing 
options and leave reviews for their current housing. This script provides 
all the logic for making adjustments to the list containing the resources 
in our app. It also contains the Property class which represents a housing 
unit.

Attributes:
        Housing (list of Properties): a list containing all the
            properties currently in our app.
"""
import random

# In-memory database (for example purposes)
housing = []

def add_listing(address, on_campus, apply):
    """ Creates a new Property object and adds it to the Housing list.

    Args:
        address (string): the addres of the listing
        on_campus (bool): True if the property is on campus, False otherwise
        apply (string): information on how to apply for listed property
    """
    if len(address) > 0 and len(apply) > 0:
        listing = Property (address, on_campus, apply)
        housing.append(listing)


def find_listing(address):
    """ Finds a specific Property object in the collection using its address.

    Args:
        address (string): the addres of the listing
        
    Returns:
        Property: returns the Property object that matches the address
    """
    for listing in housing:
            if listing.address == address.upper():
                    return listing
    return "No Location Found: please add location"

class Property:
    """ A class that represents single property listing

    Attributes:
        address (string) : the address of the listed property
        ratings (list of floats) : list of ratings (a number 1-5) given by 
                past tennents
        reviews (list of strings) : list of reviews/comments from past tennants 
                for the property
        on-campus (bool): true if the listing in on campus, false if listing is 
                off-campus
        apply (string): url or email to apply for the residence
        
    """
    def __init__(self, address, on_campus, apply):
        """Initializes a new instance of a class with specified attributes.

        Args:
            address (str): The physical address of the entity (e.g., a building 
                    or dormitory).
            on_campus (bool):  Indicates whether the entity is located on a 
                    campus (True) or off-campus (False).
            apply (function): A function or callable object that defines how to 
                    interact with the entity.
        """
        self.address = address.upper()
        self.ratings = []
        self.reviews = []
        self.on_campus = on_campus
        self.apply = apply


    def add_rating(self, rating, review):
        """ Allows for someone to rate a property. Rating is added to the 
        ratings attribute

        Args:
            rating (float): a number 1-5 that represents a person's experience 
            living at this residence
        """
        # Make sure rating is in correct range
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Rating must be between 1 and 5.")
        
        if len(review) != 0:
            self.reviews.append(review)

    def avg_rating(self):
        """ Calculates the average rating of a property

        Returns:
            float: return a average of the ratings associated with this property
        """
        if len(self.ratings) == 0:
            return 0
        sum = 0
        for x in self.ratings:
            sum += x
        return round(sum/len(self.ratings),1)
    
if __name__ == "TerpHousingHub":
    """This puts in sample data into our app so that the functionality 
    is visible and testing is easier
    """
    add_listing("5721 29th ave hyattsville, MD 20782", False, "zuly@apply.com")
    add_listing("5012 edgewood rd college park, MD 20740", True, "applyHousing.com")
    add_listing("4300 Hartwick Rd College Park, MD 20740", True, "terrapinrow.com")
    add_listing("2019 Amherst Rd hyattville, MD 20783", False, "teresaMart@gmail.com")
    add_listing("8520 63rd ave berwyn heights, MD 20740", False, "ferLucero@verizon.net")
    add_listing("8923 Regents Dr College Park, MD 20741", True, "ferLucero@verizon.net")
    add_listing("1122 berwyn st greenbelt, MD 20743", False, "callme@verizon.net")
    add_listing("5555 50th ave College Park, MD 20740", True, "abc@apply.net")
    for x in housing:
        x.add_rating(random.uniform(1.0, 5.0), "good place")
        x.add_rating(random.uniform(1.0, 5.0), "bad location")
        x.add_rating(random.uniform(1.0, 5.0), "great landlord!")