import sys

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores = {}
    afinn_file = open("AFINN-111.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

    for line in afinn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print scores.items() # Print every (term, score) pair in the dictionaryterm


if __name__ == '__main__':
    main()
