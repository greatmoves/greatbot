from urllib.request import Request, urlopen
import json, random, string, discord
from bs4 import BeautifulSoup
import os.path, time, os
from gfycat import get_gfy

def caller(subreddit, isNsfw):
    #create_reddit(subreddit)
    return read_reddit(subreddit, isNsfw)

def create_reddit(subreddit):
    try:
        if time.time() - os.path.getmtime("subreddits/" + str(subreddit) + ".json") > (60*60*24):
            f = open("subreddits/" + str(subreddit) + ".json", "w")
            req = Request("https://www.reddit.com/r/" + str(subreddit) + ".json?sort=hot", headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req)
            data = json.loads(webpage.read())
            json.dump(data, f, indent=4)
            f.close()

        else:
            return 0

    except(FileNotFoundError):
        req = Request("https://www.reddit.com/r/" + str(subreddit) + ".json?sort=hot",
                      headers={'User-Agent': 'Mozilla/5.0'})
        f = open("subreddits/" + str(subreddit) + ".json", "w")
        webpage = urlopen(req)
        data = json.loads(webpage.read())
        json.dump(data, f, indent=4)
        f.close()


def read_reddit(subreddit, isNsfw):
    req = Request("https://www.reddit.com/r/" + str(subreddit) + ".json?sort=hot",
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    data = json.loads(webpage.read())
    amount = data["data"]["dist"]
    choice = random.randint(0, amount)
    post = data["data"]["children"][choice]["data"]
    if post["over_18"] and not isNsfw or amount == 0:
        return -1
    while len(post["selftext"]) > 2000:
        choice = random.randint(0, amount)
        post = data["data"]["children"][choice]["data"]
    embed = discord.Embed(title = post["title"], url = post["url"], description = post["selftext"], colour = 0xFF00CC)
    if len(post["selftext"]) == 0:
        try:
            if post["secure_media"]["type"] == "gfycat.com":
                embed.set_image(url = get_gfy(post["url"]))
            else:
                embed.set_image(url = post["url"])
        except(TypeError):
            embed.set_image(url=post["url"])

    embed.add_field(name = "Posted by: ", value = post["author"], inline = True)
    embed.add_field(name = "Upvotes: ", value = post["ups"], inline = True)
    embed.add_field(name="Downvotes: ", value=post["downs"], inline=True)
    embed.add_field(name="Comments: ", value=post["num_comments"], inline=True)
    return embed


