from dataclasses import dataclass
from models.rating import Rating

class App:

    
    def __init__(self,data):
        self._data:object = data
    
    @property
    def id(self):
        return self._data['id']

    @property
    def data(self):
        return self._data
    
    @property
    def name(self):
        return self._data['attributes']['name']
    
    @property
    def url(self):
        return self._data['attributes']['url']

    @property
    def ratings(self) -> Rating:
        _ratings = Rating(self._data['attributes']['userRating'])

        return _ratings

    def get_reviews(self):
        raise NotImplementedError("get_reviews yet implemented")