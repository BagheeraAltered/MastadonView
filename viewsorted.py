import time
from bs4 import BeautifulSoup
from mastodon import Mastodon

# Set up your Mastodon instance URL and access token
instance_url = 'ADD INSTANCE'
access_token = 'ADD TOKEN'

# Create an instance of the Mastodon API client
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance_url
)

# Fetch the latest 500 toots
toots = mastodon.timeline_home(limit=500)

# Sort the toots by the number of reblogs (boosts)
sorted_toots = sorted(toots, key=lambda toot: toot['reblogs_count'], reverse=True)

# Print the content of the 10 most reblogged toots
#for toot in sorted_toots[:10]:
#    print(toot['content'])

# Assume 'toots' is your list of toots
for toot in toots:
    toot_content = toot['content']

    # Create a soup object
    soup = BeautifulSoup(toot_content, 'html.parser')

    # 'get_text()' extracts all the text inside the HTML tags
    plain_text = soup.get_text()

    print(plain_text)
