import appstorescraper
import logging


app_id = '284882215'
app_name = 'Facebook'

def test_getappdetails():

    try:
        app = appstorescraper.AppStoreScraper.get_app(app_id)

        logging.info(f'App name: {app.name} | App ID: {app.id}')
        assert app.name == app_name

    except Exception as e:
        logging.error(e)
        assert False

    
def test_getappratings():
    try:
        app = appstorescraper.AppStoreScraper.get_app(app_id=app_id)
        logging.info(f'App name: {app.name} | App ID: {app.id} | Ave rating: {app.ratings.average}')
        logging.info('1-star:{0} | 2-star:{1} | 3-star: {2} | 4-star: {3} | 5-star: {4}'.format(*app.ratings.list))
        assert True

    except Exception as e:
        logging.error(e)
        assert False



    