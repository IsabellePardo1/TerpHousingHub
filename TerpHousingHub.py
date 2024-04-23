""" 
This script allows for UMD students to browse through student housing 
options and leave reviews for their current housing.

Attributes:
        Housing (list of Properties): a list containing all the
            properties currently in our database of hosing options.
"""
housing = []

def add_listing(address, on_campus, apply):
    """ Creates a new Property object and adds it to the Housing list.

    Args:
        address (string): the addres of the listing
        on_campus (bool): True if the property is on campus, False otherwise
        apply (string): information on how to apply for listed property
    """
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
                if listing.address == address:
                        return listing
        return None

def browse(on_campus, min_rating):
    """ Finds as many listings of Properties that fit the specifications of the parameters.
        If on_campus is True only listings on campus will be returned. If min_rating is 2.5 
        only Properties with a rating of 2.5 or more will be returned.

    Args:
        on-campus (boolean): True if listing should be on campus, False if listing should be off campus
        min-rating (float): the minimum rating a listing should have

    Returns:
        list: returns a list of properties that match the specifications
    """
    pass

class Property:
    """ A class that represents single property listing

    Attributes:
        address (string) : the address of the listed property
        ratings (list of floats) : list of ratings (a number 1-5) given by past tennents
        on-campus (bool): true if the listing in on campus, false if listing is off-campus
        apply (string): url or email to apply for the residence
        
    """
    def __init__(self, address, on_campus, apply):


    def add_rating(self, rating):
        """ Allows for someone to rate a property. Rating is added to the ratings attribute

        Args:
            rating (float): a number 1-5 that represents a person's experience 
            living at this residence
        """
        # Make sure rating is in correct range
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Rating must be between 1 and 5.")

    def avg_rating(self):
        """ Calculates the average rating of a property

        Returns:
            float: return a average of the ratings associated with this property
        """
        sum = 0
        for x in self.ratings:
            sum += x
        return (sum/len(self.ratings))
