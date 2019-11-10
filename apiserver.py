# Import your handlers here
from service import Titanic, Intro


# Configuration for web API implementation
def config(api):
    # Instantiate handlers
    intro = Intro()
    titanic = Titanic()

    # Map routes
    api.add_route('/titanic', intro)
    api.add_route('/titanic/{index:int(min=0)}', titanic)
