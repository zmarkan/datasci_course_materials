import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

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

def main():
    scores = {}

    sent_file_name = sys.argv[1]

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for tweet_line in tweet_file:
        tweet = json.loads(tweet_line)
        print calculateSentiment(tweet, scores)

if __name__ == '__main__':
    main()
