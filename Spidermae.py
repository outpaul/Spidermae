# This spider downloads memes from subreddits with all the
# settings being mentioned in the settings.py file.

# This script does not use PRAW since it only retrieves memes from the
# subreddits, there is no user interaction with the website so I didn't see
# it fit to use an API.

import os
import requests
import re
import shutil
import threading

from settings import subreddits

sublist = subreddits()

def jpath(dir,name = ''):
    return os.path.join(sublist[1],dir,name)

def subreddit(sub):

    count = "1"

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

            image = requests.get(link[0], headers = {'User-agent' : 'Spidermae Bot'}, stream=True)
            if image.status_code == requests.codes.ok:
                filename = count + '.' + link[1]
                with open(jpath(sub,filename),'wb') as img:
                    shutil.copyfileobj(image.raw, img)
                print("\nDownloaded " + sub + "/" + filename + " successfully.")
                count = str(int(count) + 1)
            else:
                print("There was a problem retrieving one of the images!\n Check your Internet connection and try again.")
    else:
        print("There was a problem retrieving r/" + sub + "!\nPlease check your Internet connection or the settings.py file for invalid subreddits.")

jobs = []

# I write this code here instead of the next loop because
# I don't want a long gap between each thread's start time

for sub in sublist[0]:
    # Due to different file extensions sometimes all the files don't get overwritten
    # so as a precautionary measure we delete the files already in the folders
    for file in os.listdir(jpath(sub)):
        fileName = jpath(sub,file)
        try:
            if os.path.isfile(fileName):
                os.unlink(fileName)
        except Exception as err:
            print(err)

for i in range(len(sublist[0])):
    j = threading.Thread(target=subreddit, args=(sublist[0][i],))
    jobs.append(j)
    jobs[i].start()

for job in jobs:
    job.join()

print("\n\nDone!\n\n")
