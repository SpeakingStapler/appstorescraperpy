from models.rating import Rating
from models.reviews import Reviews
from models.review import Review
from typing import List

from core import AppleScraper

class App:

    def __init__(self,data,country):
        self.__data:object = data
        self.__country = country
        self.__reviews:Reviews = None
    
    @property
    def id(self):
        return self.__data['id']

    @property
    def country(self):
        return self.__country

    @property
    def data(self):
        return self.__data
    
    @property
    def name(self):
        return self.__data['attributes']['name']
    
    @property
    def url(self):
        return self.__data['attributes']['url']

    @property
    def ratings(self) -> Rating:
        _ratings = Rating(self.__data['attributes']['userRating'])

        return _ratings

    @property
    def reviews(self) -> Reviews:

        if not self.__reviews:
            self.__reviews = Reviews(self)

        return self.__reviews
    

    def get_reviews(self,count=20,offset=0) -> tuple[List['Review'], int]:
        review_data = AppleScraper._get_app_reviews_per_country(self.id,self.country,count,offset)
        
        reviews = []
        for data in review_data[0]:
            reviews.append(Review(data, self))
        return reviews, review_data[1]

    
