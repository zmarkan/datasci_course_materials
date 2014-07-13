import sys
import json

class Term:
    def __init__(self, term):
        self.term = term
        self.occurences = 0

def parseTweets(tweet_file):
    tweets = []
    for tweet_line in tweet_file:
        tweet = json.loads(tweet_line)
        if "text" in tweet:
            tweets.append(tweet["text"])
    return tweets

def createWordList(line):
    wordList2 =[]
    wordList1 = line.split()
    for word in wordList1:
        cleanWord = ""
        for char in word:
            if char in '!,.?":;':
                char = ""
            cleanWord += char
        wordList2.append(cleanWord)
    return wordList2

def main():
    tweet_file = open(sys.argv[1])

    tweets = parseTweets(tweet_file)

    all_terms = {}
    all_terms_in_all_tweets = 0

    for tweet in tweets:
        word_list = createWordList(tweet)

        all_terms_in_all_tweets = all_terms_in_all_tweets + len(word_list)

        for term in word_list:
            if not term in all_terms:
                all_terms[term] = Term(term)
            all_terms[term].occurences = all_terms[term].occurences + 1

    if all_terms_in_all_tweets == 0:
        all_terms_in_all_tweets = 1

    for term in all_terms:
        term_object = all_terms[term]
        frequency = term_object.occurences / float(all_terms_in_all_tweets)
        print term_object.term + " " + str(frequency)


if __name__ == '__main__':
    main()
