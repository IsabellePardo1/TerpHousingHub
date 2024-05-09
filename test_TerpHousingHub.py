import pytest
import TerpHousingHub
from TerpHousingHub import Property

def test_property():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    assert isinstance(apt, Property)

def test_add_rating():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    apt.add_rating(5, 'good')
    assert (apt.ratings[0] == 5 and apt.reviews[0] == 'good')

def test_avg_rating():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    apt.add_rating(5, 'best place ever')
    apt.add_rating(3, 'not bad')
    assert (apt.avg_rating() == 4)

def test_add_listing():
    TerpHousingHub.add_listing("8520 Regents Drive College Park, MD 20740", True, "apply on umd.housing.com")
    assert (len(TerpHousingHub.housing) == 9)

def test_find_listing():
    assert(TerpHousingHub.find_listing("random") == "No Location Found: please add location")

def test_find_listing2():
    TerpHousingHub.add_listing("9999 library ln College Park, MD 20740", True, "umd.housing.com")
    assert(TerpHousingHub.find_listing("9999 library ln College Park, MD 20740").address == "9999 LIBRARY LN COLLEGE PARK, MD 20740")

 