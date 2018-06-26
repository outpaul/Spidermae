# This spider downloads memes from subreddits with all the
# settings being mentioned in the settings.py file.

# This script does not use PRAW since it only retrieves memes from the
# subreddits, there is no user interaction with the website so I didn't see
# it fit to use an API.

import os
import requests
import re
import shutil

from settings import subreddits

def jpath(dir,name = ''):
    return os.path.join(os.getcwd(),dir,name)

sublist = subreddits()

os.chdir(sublist[1])

for sub in sublist[0]:
    count = '1'
    if not os.path.isdir(jpath(sub)):
        os.makedirs(jpath(sub))

    url = "https://www.reddit.com/r/"+sub+"/top?t=week"
    print("\n\nDownloading from r/"+sub+"...\n\n")
    page = requests.get(url, headers = {'User-agent' : 'Spidermae Bot'})

    if page.status_code == requests.codes.ok:
        exp = re.compile(r'(https://i.redditmedia.com/[\w\-]*\.(\w+)\?s\=\w+)\"')
        links = list(set(re.findall(exp, page.text)))

        for link in links:
            if count == "21":
                break
            print("\nDownloading meme...")
            image = requests.get(link[0], headers = {'User-agent' : 'Spidermae Bot'}, stream=True)
            if image.status_code == requests.codes.ok:
                filename = count + '.' + link[1]
                with open(jpath(sub,filename),'wb') as img:
                    shutil.copyfileobj(image.raw, img)
                print("\nDownloaded " + filename + " successfully.")
                count = str(int(count) + 1)
            else:
                print("There was a problem retrieving one of the images!\n Check your Internet connection and try again.")
    else:
        print("There was a problem retrieving r/" + sub + "!\nPlease check your Internet connection or the settings.py file for invalid subreddits.")

print("\n\nDone!\n\n")
