import sys
import json

__author__ = 'Harshali'


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    term_dict = {}
    tweet_text = []
    term_total = 0

    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            tweet_text.append(tweet['text'].lower().encode('utf-8'))

        for tweet in tweet_text:
            tweet_words = tweet.split()

            for word in tweet_words:
                word = word.rstrip('?:!.,;"!@')
                word = word.replace("\n", "")

                if word in term_dict:
                    term_dict[word] += 1
                else:
                    term_dict[word] = 1
                term_total += 1

    for x in sorted(term_dict, key=term_dict.get):
        print x, ' ', term_dict[x]/term_total

if __name__ == '__main__':
    main()

