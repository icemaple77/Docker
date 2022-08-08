import nltk
from nltk import FreqDist
nltk.download('gutenberg')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
from flask import Flask
app = Flask(__name__)

@app.route("/")
def count_words():
    stopWords = set(stopwords.words('english'))
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopWords]
    fdist = FreqDist(tokens)
    common = fdist.most_common(500)
    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()
    highCount = common[0][1]
    contents=' '
    for word in words:
        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / \
        float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
              colour = "0" + colour
        contents= contents+'<span style="font-size:'+ size + 'px; color: #'+ colour + '">'+ word + '</span>'+' '
    return  '<html><head><title>Common Words</title></head><body>'+contents+'</body></html>'

if __name__ == "__main__":
    app.run()