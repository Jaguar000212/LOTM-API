'''
Struncture for character objects.
'''

import requests
import bs4
import api.helpers as helpers

web_url = "https://lordofthemysteries.fandom.com/wiki/"


class CharacterStructure:
    
    '''CharacterStructure is the base class for all character objects.'''
    
    def __init__(self, name : str):
        self.url_name = helpers.misc.format_name(name)
        self.url = web_url + self.url_name
        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            raise helpers.exceptions.NotFoundError("Character not found.")
        
        self.parsed = bs4.BeautifulSoup(self.response.text, 'html.parser')
        self.name = self.get_name()
        
    def get_name(self):
        
        '''Returns the name of the character as on the webpage.'''
        
        pass
    
    def get_data(self) -> dict:
        
        '''Returns a dictionary of the character's data.'''
        
        data = self.__dict__
        data.pop("response")
        data.pop("parsed")
        data.pop("url_name")
        
        return data
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value
