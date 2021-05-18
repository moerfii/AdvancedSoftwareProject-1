import pytest
from restAPIConnection.restAPIConnection import RestAPIConnection


#only work in travis
#uses RestAPIConnection with no arguments
@pytest.fixture
def RAC_empty():
    return RestAPIConnection()


def test_getListingLocation_empty(RAC_empty):
    l = [None]
    RAC_empty.getListingLocations(l)
    assert (len(l[0])==2)

def test_getListingLocation_filter(RAC_empty):
    l = [None]
    custom_filter = {'borough.eq':'Bronx'}
    RAC_empty.getListingLocations(l,custom_filter)
    assert (len(l[0])==1)

def test_getListingDetail_empty(RAC_empty):
    l = [None]
    RAC_empty.getListingDetail(l)
    assert (len(l[0])==1)

def test_getListingDetail_filter(RAC_empty):
    l = [None]
    custom_filter = {'id.eq':-1}
    RAC_empty.getListingDetail(l,custom_filter)
    assert (len(l[0])==0)

def test_getListingOther_empty(RAC_empty):
    l = [None]
    RAC_empty.getListingOther(l)
    assert (len(l[0])==1)

def test_getListingOther_filter(RAC_empty):
    l = [None]
    custom_filter = {'id.eq':-1}
    RAC_empty.getListingOther(l,custom_filter)
    assert (len(l[0])==0)

def test_getVillageCategory_empty(RAC_empty):
    l = [None]
    RAC_empty.getVillageCategory(l)
    assert (len(l[0])==3)

def test_getVillageCategory_filter(RAC_empty):
    l = [None]
    custom_filter = {'category.in[]': ['Nightlife','Art & Music']}
    RAC_empty.getVillageCategory(l,custom_filter)
    assert (len(l[0])==2)