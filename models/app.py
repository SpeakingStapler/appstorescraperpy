from models.rating import Rating
from models.reviews import Reviews

class App:

    def __init__(self,data,country):
        self._data:object = data
        self.country = country
        self._reviews:Reviews = None
    
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

    @property
    def reviews(self) -> Reviews:

        if not self._reviews:
            self._reviews = Reviews(self)

        return self._reviews
    

    def get_reviews(self,count=100):

        raise NotImplementedError("get_reviews yet implemented")
    
