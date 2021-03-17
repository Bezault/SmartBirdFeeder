#Fetch images from flickr and upload it to roboflow
from flickr_scraper import get_url_simple
import requests
import urllib.parse

search_text = ['common starling',
                'goldfinch',
                'chaffinch',
                'wood pigeon',
                'magpie',
                'carrion crow',
                'jay bird',
                'wren',
                'goldcrest bird',
                'dunnock',
                'coal tit',
                'great tit',
                'long-tailed tit',
                'greenfinch',
                'song thrush',
                ]

for text in search_text:
    img_urls = get_url_simple(search=text,n=100)
    j=0
    for img_url in img_urls:
        img_name = "&name="+text+str(j)
        upload_url = "".join([
            "https://api.roboflow.com/dataset/birds-3emme/upload",
            "?api_key=xxxx",
            img_name,
            "&split=train",
            "&image=" + urllib.parse.quote_plus(img_url)
        ])
        print(j)
        print(upload_url)
        # POST to the API
        j=j+1

        try:
            r = requests.post(upload_url)

            # Output result
            print(r.status_code)
            print(r.json())
        except:
            print("Request error")