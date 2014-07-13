import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


class Tweet:
    pass

def parseTweets(tweet_file):
    tweets = []
    for tweet_line in tweet_file:
        tweet = json.loads(tweet_line)
        if "coordinates" in tweet:
            print tweet["coordinates"]
        if "place" in tweet:
            print tweet["place"]
        if "user" in tweet:
            print tweet["user"]["location"]
            # if "location" in tweet:
            #     newTweet = Tweet()
            #
            #     # tweets.append(tweet["text"])
            #     newTweet.text = tweet["text"]
            #     newTweet.location = tweet["location"]
            #     tweets.append(netTweet)
    return tweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    tweets = parseTweets(tweet_file)
    for tweet in tweets:
        print tweet.text
        print tweet.location


    pass

if __name__ == '__main__':
    main()
