from product_scraper import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':

    visit_url = "https://www.trendyol.com/sr?tag=kirmizi_kampanya_urunu%2Cturuncu_kampanya_urunu&sst=BEST_SELLER"

    scraper = ProductProvider()

    scraper.GetPageProducts(visit_url)
