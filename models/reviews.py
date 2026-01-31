from models.review import Review
from core import AppleScraper
import logging

class Reviews:

    def __init__(self, app):
        self.app = app
        self._current_data = {}

        self._current_offset = 0
        self._current_iter = 0
        self._reviews = []
    
    def __len__(self):
        return len(self._reviews)

    def __getitem__(self, key:int) -> Review:
        last_review_count = 0
        while len(self._reviews) < key:
            self.__iterate()
            
            if len(self._reviews) > key:
                break
            
            if last_review_count == len(self._reviews):
                raise IndexError(f'Cannot retrieve more than {key} reviews')
            
            last_review_count = len(self._reviews)
        
        return self._reviews[key]
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Review:

        if self._current_iter >= len(self._reviews):
            self.__iterate()
        
        review:Review = self._reviews[self._current_iter]

        self._current_iter += 1

        return review
    
    def __iterate(self):
        logging.debug(f'Retrieving reviews data for app {self.app.name} | Current offset: {self._current_offset}')
        self._current_data = AppleScraper._get_app_reviews_per_country(self.app.id,self.app.country,20,self._current_offset)
        self._current_offset = self._current_data[1]

        for review_data in self._current_data[0]:
            self._reviews.append(Review(review_data,self.app))



        

    

    
