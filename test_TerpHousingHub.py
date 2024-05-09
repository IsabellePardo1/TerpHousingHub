"""Tests functionality of the app located in TerpHousingHub.py
"""
import pytest
import TerpHousingHub
from TerpHousingHub import Property

def test_property():
    """Tests the ability to create Property objects
    """
    apt = Property("5721 63rd ave College Park, MD, 20740", 
                    False, 
                    "email 123rentals@gmail.com for applications")
    assert isinstance(apt, Property)

def test_add_rating():
    """Tests the ability to add ratings and reviews to Property objects
    """
    apt = Property("5721 63rd ave College Park, MD, 20740", 
                    False, 
                    "email 123rentals@gmail.com for applications")
    apt.add_rating(5, 'good')
    assert (apt.ratings[0] == 5 and apt.reviews[0] == 'good')

def test_avg_rating():
    """Tests the ability to calculate the average of all ratings for a property
    """
    apt = Property("5721 63rd ave College Park, MD, 20740", 
                    False, 
                    "email 123rentals@gmail.com for applications")
    apt.add_rating(5, 'best place ever')
    apt.add_rating(3, 'not bad')
    assert (apt.avg_rating() == 4)

def test_add_listing():
    """Makes sure that add_listing() appends property to housing list
    """
    TerpHousingHub.add_listing("8520 Regents Drive College Park, MD 20740", 
                                True, 
                                "apply on umd.housing.com")
    assert (len(TerpHousingHub.housing) == 9)

def test_find_listing():
    """Tests is proper message is returned when listing is not found
    """
    expected_msg = "No Location Found: please add location"
    assert(TerpHousingHub.find_listing("random") == expected_msg)

def test_find_listing2():
    """Tests if proper object is returned when calling find_listing()
    """
    address = "9999 library ln College Park, MD 20740"
    TerpHousingHub.add_listing(address, True, "umd.housing.com")
    assert(TerpHousingHub.find_listing(address).address == address.upper())

 