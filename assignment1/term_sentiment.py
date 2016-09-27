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
    sent_scores = {} #initialize an empty dictionary
    tweet_scores = {}
    tweet_text = []
    new_words = []

    for line in sent_file:
        term, score = line.split("\t") #The file is tab de-limited.
        sent_scores[term] = int(score) #Convert the score to an integer

    #print scores.items()

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

            if word in sent_scores.keys():
                sentiment = sentiment + sent_scores[word]
            else:
                new_words.append(word)

        tweet_scores[tweet] = int(sentiment)

    for term in new_words:
        pos = neg = total = 0
        for tweet in tweet_scores:
            if term in tweet:
                if tweet_scores[tweet] > 0:
                    pos += 1
                elif tweet_scores[tweet] < 0:
                    neg += 1
                total += 1
        print term, ' ', (pos-neg)/total


    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
