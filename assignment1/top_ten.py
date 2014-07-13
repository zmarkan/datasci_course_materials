import sys
import json

class Hashtag:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.occurences = 0
    pass

def parseTweets(tweet_file):
    all_hashtags = {}
    for tweet_line in tweet_file:
        tweet = json.loads(tweet_line)
        if "entities" in tweet:
            entities = tweet["entities"]
            for hashtag in entities["hashtags"]:
                hashtag_text = hashtag["text"]

                if not hashtag_text in all_hashtags:
                    all_hashtags[hashtag_text] = Hashtag(hashtag_text)
                    all_hashtags[hashtag_text].occurences = all_hashtags[hashtag_text].occurences + 1

    return all_hashtags

def main():

    tweet_file = open(sys.argv[1])

    all_hashtags = parseTweets(tweet_file)

    hashtags_list = []

    for hashtag in all_hashtags:
        hashtags_list.append(all_hashtags[hashtag])

    sorted_list = sorted(hashtags_list, key=lambda hashtag: hashtag.occurences)

    counter = 0
    while counter < 10:
        hashtag = sorted_list[counter]
        print hashtag.hashtag + " " + str(hashtag.occurences)
        counter = counter + 1


if __name__ == '__main__':
    main()
