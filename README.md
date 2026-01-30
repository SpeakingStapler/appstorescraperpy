# appstorescraperpy
Apple App Store Scraper written in python

## Apple App Store Scraper
This is based on cowboy-bebug's <a href='https://github.com/cowboy-bebug/app-store-scraper'>app-store-scraper </a> (now deprecated) as this is the only project I've seen that is able to retrieve all the App Store reviews. Unfortunately it can only retrieve reviews and not ratings and other project details, which I implemented in the custom module.

I initially used this on an Azure Function and I did not implement custom classes and let the caller parse the JSON data themselves. This iteration I plan to include classes to handle the data