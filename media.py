#This module defines the class Movie, which is passed a title. The title is
#then used to query the ODB API to return other information about the movie
import requests

class Movie():
    #Assigning API end point and access key details as Class Attributes
    OMDb_path = 'http://www.omdbapi.com/'
    apikey = '73cd8d95'
    #Assigning Instance Attributes, Individual Movie attributes are derived by
    #passing parameter to get_info method
    def __init__(self, title, trailer):
        self.__name__ = title
        self.title = title
        self.trailer = trailer
        self.alldata = self.get_info
        self.plot = self.get_info('Plot')
        self.year = self.get_info('Year')
        self.poster = self.get_info('Poster')
    #Class Method for querying the OMDB API. Call with no parameter for all
    #data. Call with parameter for specific data
    def get_info(self, querytype):
        response = requests.get(self.OMDb_path, params={'apikey':self.apikey,
                                                        't': self.title})
        self.alldata = response.json()
        if querytype == "":
            return {self.alldata}
        else:
            return self.alldata.get(querytype)
    