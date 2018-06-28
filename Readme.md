# **Spidermae**

Spidermae is a spider which downloads memes from the subreddits of your choice.

It is a cross-platform script which uses multithreading and web crawling to obtain the image, audio or video files from your favourite subreddits and stores it right where you want it to.

_This script is written in **python3** so please make sure you use the **python3** interpreter._


## Pre-requisites

There are some third-party python libraries used in this script which do not come bundled with the standard python packages.

The following packages are:

- requests: Download the *requests* library by pasting the following code in your terminal
```
pip install requests
```

- shutil: Download the *shutil* library by pasting the following code in your terminal
```
pip install shutil
```

## Settings

Modify the *settings.py* file and enter the subreddits where you want to download your memes from. You can also specify the directory in which you want your memes to be stored.
For the script to run at regular intervals enter the time interval(in hours) at which you want the script to run.

## Usage

To run the script once run the following command on your terminal:

```
python3 Spidermae.py
```

To run the script regularly after your specified intervals run the following command:

```
python3 run.py
```
