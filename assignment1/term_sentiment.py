import sys
import json

class Term:
    def __init__(self, term):
        self.term = term
        self.occurences = 0
        self.score = 0

class Tweet:
    pass

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

def calculateSentiment(tweet, scores):
    sentiment = 0
    if "text" in tweet:
        text = tweet["text"]
        word_list = createWordList(text)
        for word in word_list:
            if word in scores:
                sentiment = sentiment + scores[word]
                break
    return sentiment

def sentimentOfText(text, scores):
    sentiment = 0
    word_list = createWordList(text)
    for word in word_list:
        if word in scores:
            sentiment = sentiment + scores[word]
            break
    return sentiment


def isWordInTweet(word, tweet):
    if "text" in tweet:
        text = tweet["text"]
        word_list = createWordList(text)
        if word in word_list:
            return true
    return false

def isWordInSentiment(word, sentiment):
    if word in sentiment:
        return True
    else:
        return False

def calculateScores(sentiment_file):
    scores = {}
    for line in sentiment_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def parseTweets(tweet_file):
    tweets = []
    for tweet_line in tweet_file:
        tweet = json.loads(tweet_line)
        if "text" in tweet:
            newTweet = Tweet()
            tweets.append(tweet["text"])
    return tweets

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = calculateScores(sent_file)
    tweets = parseTweets(tweet_file)

    all_terms = {}

    all_terms["soccer"] = Term("soccer")
    all_terms["soccer"].score = 2



    for tweet in tweets:
        word_list = createWordList(tweet)
        for word in word_list:
            if not isWordInSentiment(word, scores):
                if not word in all_terms:
                    all_terms[word] = Term(word)
                all_terms[word].score = sentimentOfText(tweet, scores)
                all_terms[word].occurences = all_terms[word].occurences + 1

    for term in all_terms:
        instance = all_terms[term]
        if instance.occurences == 0:
            instance.occurences = 1
        avg_score = instance.score / float(instance.occurences)
        print instance.term + " " + str(avg_score)

if __name__ == '__main__':
    main()
