import requests
import json
import time

class RestAPIConnection:
    """
    """
    def __init__(self,filters=None,base_url="http://localhost:8888"):
        self.base_url=base_url
        self.filters= {}
        self.filters = self.overrideFilter(filters)

    

    def overrideFilter(self,custom_filters=None):
        filters = self.filters.copy()
        if custom_filters:
            for key in custom_filters.keys():
                filters[key] = custom_filters[key]
        filters = {k: v for k, v in filters.items() if v is not None}
        return filters

    def _GET(self,res,url,custom_filters,append):
        if append:
            filters = self.overrideFilter(custom_filters)
        else:
            filters = custom_filters
        res[0] = json.loads(requests.get(url,params=filters).text)

    def getListingLocations(self,res,custom_filters=None,append=True):
        url=self.base_url+"/listing_location"
        self._GET(res,url, custom_filters,append)
    
    def getListingDetail(self,res,custom_filters=None,append=True):
        url=self.base_url+'/listing_detail'
        return self._GET(res,url, custom_filters,append)
    
    def getListingOther(self,res,custom_filters=None,append=True):
        url = self.base_url+'/listing_other'
        return self._GET(res,url, custom_filters,append)
