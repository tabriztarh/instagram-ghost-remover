## Instagram Ghost Remover

A tool that will remove followers that haven't liked or commented on a single post of yours.

### Why?

Even though people are trying to increase their follower count, the quality of their followers may decrease. It is not uncommon to see people with 50K followers but only ~1500 likes at their posts. This tool aims to remove low-quality followers from your account.

### How does it work?

The tool will load all of your followers, all of your posts, all likes under the posts and all comments under the posts. Then, it will count all the likes and comments under your posts from your followers. At the end of the process, if a follower does not have any likes or comments, they'll be marked as a ghost. Finally it will force them out of your follower list by blocking and unblocking them. The whole process may take minutes to days, depending on the number of your followers. You may pause and resume it though (in case you need to turn your computer off in the middle).

## Usage (tried to make it easy for non savvy people)

 - Download this repo (this whole thing) as ZIP and unzip it.
 - Open your terminal. (On Mac: open the Terminal app, on Windows, open Command Prompt, on Linux, well you probably know what you are doing anyway ;))
 - Check Python version. (On Mac: type `python -V`, on Windows, type `python`. Press Enter. If you see something like Python 2.7 (I've tested on 2.7.10) great. If you get an error or see a Python 3.x version, download Python 2.7 (Google it). (Would it work with Python 3? Maybe, but I didn't test it.)
 - Go to the folder that you unzipped this repo from the terminal. (Type `cd full_path_to_your_folder`, for example `cd C:\Downloads\instagram-ghost-remover` or `cd /Users/Name/Downloads/instagram-ghost-remover`. Of course these are just examples. You can just type `cd ` (with a space after it) and drag-drop your folder into the terminal window to paste the full path to it). Press Enter.
 - Type `pip install -r requirements-dev.txt`. Press Enter. It may take about a minute to complete. When it stops downloading stuff and waits for you again, it's done.
 - Type `python start.py`. Press Enter.
 - After that point, the whole thing is self explanatory. It will load a list of your followers, posts, likes your your posts, and comments on your posts. It may take a while (e.g. minutes, or about an hour or more if you've got lots of followers/posts etc). When it's done it will start blocking/unblocking those "ghost" followers that I explained earlier. You may stop (if you think it's enough or if you need to pause) when it starts blocking/unblocking by simply closing the terminal window.

 ## Warning

 The folder will contain your username and password in the file `credentials.py` and `credentials.pyc`. Make sure those two files are safe from other people.

 ## Notes

  - The tool may not load more than 1000 likes for a single post. In 99% of the cases, I think we can ignore it.
  - To avoid API limiting (Instagram doesn't allow too many actions in a short time) the tool waits randomly between blocks. If you get an API rate limit error, simply wait about an hour and run again.
  - I am not a Python programmer, I'm just getting used to it. Some parts of the code may be terrible. Sorry for that :)

 ## Resuming after stopping

 If you've stopped the tool and want to resume:

  - Open your terminal.
  - Go to the folder with the unzipped files again.
  Type `python remove_ghost_followers.py`. Press Enter. It should resume.

---

# Below is the original readme for Instagram Private API (not written by me):

# Instagram Private API

A Python wrapper for the Instagram private API with no 3rd party dependencies. Supports both the app and web APIs.

![Python 2.7, 3.5](https://img.shields.io/badge/Python-2.7%2C%203.5-3776ab.svg?maxAge=2592000)
[![Release](https://img.shields.io/github/release/ping/instagram_private_api.svg?colorB=ff7043)](https://github.com/ping/instagram_private_api/releases)
[![Docs](https://img.shields.io/badge/docs-readthedocs.io-ff4980.svg?maxAge=2592000)](https://instagram-private-api.readthedocs.io/en/latest/)
[![Build](https://img.shields.io/travis/ping/instagram_private_api.svg)](https://travis-ci.org/ping/instagram_private_api)

[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/ping)

## Overview

I wrote this to access Instagram's API when they clamped down on developer access. Because this is meant to achieve [parity](COMPAT.md) with the [official public API](https://www.instagram.com/developer/endpoints/), methods not available in the public API will generally have lower priority.

Problems? Please check the [docs](https://instagram-private-api.readthedocs.io/en/latest/) before submitting an issue.

## Features

- Supports many functions that are only available through the official app, such as:
    * Multiple feeds, such as [user feed](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.user_feed), [location feed](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.feed_location), [tag feed](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.feed_tag), [popular feed](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.feed_popular)
    * Post a [photo](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.friendships_destroy) or [video](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.post_video) to your feed or stories
    * [Like](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.comment_like)/[unlike](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.comment_unlike) posts
    * Get [post comments](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.media_comments)
    * [Post](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.post_comment)/[delete](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.Client.delete_comment) comments
    * [Like](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.comment_like)/[unlike](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.comment_unlike) comments
    * [Follow](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.friendships_create)/[unfollow](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.friendships_destroy) users
    * User [stories](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client.user_story_feed)
    * And [more](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.Client)!
- The web api client supports a subset of functions that do not require login, such as:
    * Get user [info](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.Client.user_info) and [feed](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.Client.user_feed)
    * Get [post comments](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.Client.media_comments)
    * And [more](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.Client)!
- Compatible with functions available through the public API using the ClientCompatPatch ([app](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_private_api.ClientCompatPatch)/[web](https://instagram-private-api.readthedocs.io/en/latest/api.html#instagram_web_api.ClientCompatPatch)) utility class
- Beta Python 3 support

An [extension module](https://github.com/ping/instagram_private_api_extensions) is available to help with common tasks like pagination, posting photos or videos.

## Documentation

Documentation is available at https://instagram-private-api.readthedocs.io/en/latest/

## Install

Install with pip:

``pip install git+https://git@github.com/ping/instagram_private_api.git@1.5.7``

To update:

``pip install git+https://git@github.com/ping/instagram_private_api.git@1.5.7 --upgrade``

To update with latest repo code:

``pip install git+https://git@github.com/ping/instagram_private_api.git --upgrade --force-reinstall``

Tested on Python 2.7 and 3.5.

## Usage
The [app API client](instagram_private_api/) emulates the official app and has a larger set of functions. The [web API client](instagram_web_api/) has a smaller set but can be used without logging in.

Your choice will depend on your use case.

The [``examples/``](examples/) and [``tests/``](tests/) are a good source of detailed sample code on how to use the clients, including a simple way to save the auth cookie for reuse.

### Option 1: Use the [official app's API](instagram_private_api/)

```python

from instagram_private_api import Client, ClientCompatPatch

user_name = 'YOUR_LOGIN_USER_NAME'
password = 'YOUR_PASSWORD'

api = Client(user_name, password)
results = api.feed_timeline()
items = [item for item in results.get('feed_items', [])
         if item.get('media_or_ad')]
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item['media_or_ad'])
    print(item['media_or_ad']['code'])
```


### Option 2: Use the [official website's API](instagram_web_api/)

```python

from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError

# Without any authentication
web_api = Client(auto_patch=True, drop_incompat_keys=False)
user_feed_info = web_api.user_feed('329452045', count=10)
for post in user_feed_info:
    print('%s from %s' % (post['link'], post['user']['username']))
    
# Some endpoints, e.g. user_following are available only after authentication
authed_web_api = Client(
    auto_patch=True, authenticate=True,
    username='YOUR_USERNAME', password='YOUR_PASSWORD')
    
following = authed_web_api.user_following('123456')
for user in following:
    print(user['username'])
    
# Note: You can and should cache the cookie even for non-authenticated sessions.
# This saves the overhead of a single http request when the Client is initialised.    
```

### Avoiding Re-login
You are advised to persist/cache the auth cookie details to avoid logging in every time you make an api call. Excessive logins is a surefire way to get your account flagged for removal. It's also advisable to cache the client details such as user agent, etc together with the auth details.

The saved auth cookie can be reused for up to **90 days**.

## Donate

Want to keep this project going? Please donate generously [https://www.buymeacoffee.com/ping](https://www.buymeacoffee.com/ping)

[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/ping)

## Support
Make sure to review the [contributing documentation](CONTRIBUTING.md) before submitting an issue report or pull request.

## Legal

Disclaimer: This is not affliated, endorsed or certified by Instagram. This is an independent and unofficial API. Strictly **not for spam**. Use at your own risk.
