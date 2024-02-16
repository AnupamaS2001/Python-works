

f1_read=open("C:\\Users\\anupa\\OneDrive\\Desktop\\python_works\\file\\news.txt")
f2_read=open("C:\\Users\\anupa\\OneDrive\\Desktop\\python_works\\file\\stopwords.txt")

# nlp(natural language processing)
news_word=set()

stop_words={line.rstrip("\n") for line in f2_read}
for line in f1_read:
    words=line.split()
    for w in words:
        news_word.add(w)

print(news_word.difference(stop_words))