import sys
from random import choice


class MarkovMachine(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        body = ""

        for filename in filenames:
            text_file = open(filename)
            body = body + text_file.read()
            text_file.close()

        self.make_chains(body)

    def make_chains(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        self.chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in self.chains:
                self.chains[key] = []

            self.chains[key].append(value)

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(self.chains.keys())
        words = [key[0], key[1]]
        char_limit = 139
        text = ""

        while key in self.chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.
            while text == "" and key[0][0].islower():
                key = choice(self.chains.keys())
                words = [key[0], key[1]]


            word = choice(self.chains[key])
            # print "this is len(text): {}".format(len(text))
            # print "this is len(word): {}".format(len(word))
            if len(text) + len(word) <= char_limit:
                words.append(word)
                key = (key[1], word)
            else:
                text = text + '.'
                break

            text = " ".join(words)
            if '.' in word:
                break    

        # This is the clumsiest way to make sure it's never longer than
        # 140 characters; can you think of better ways?
        return text

if __name__ == "__main__":
    filenames = sys.argv[1:]

    generator = MarkovMachine()
    generator.read_files(filenames)
    print generator.make_text()