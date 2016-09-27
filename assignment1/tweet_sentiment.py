import sys
import json

__author__ = 'Harshali'


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()

    scores = {} #initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t") #The file is tab de-limited.
        scores[term] = int(score) #Convert the score to an integer

    #print scores.items()

    tweet_text = []
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            tweet_text.append(tweet['text'].lower().encode('utf-8'))

    for tweet in tweet_text:
        sentiment = 0
        tweet_words = tweet.split()

        for word in tweet_words:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "")
            if scores.has_key(word):
                sentiment = sentiment + scores[word]

        print sentiment

    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
