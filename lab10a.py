from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

messages = [
    ("Congratulations! You have won a free iPhone, click here to claim", "spam"),
    ("WIN cash prize now!!! Limited offer, reply YES", "spam"),
    ("Get cheap loans instantly, no documents required", "spam"),
    ("You have been selected for a free holiday, call now", "spam"),
    ("Claim your reward points before they expire, click the link", "spam"),
    ("Exclusive deal: 70% discount on all products today only", "spam"),
    ("Urgent! Your account is blocked, verify your password now", "spam"),
    ("Free entry in weekly lucky draw, text WIN to 8080", "spam"),
    ("Earn money from home, guaranteed income, join free", "spam"),
    ("Lowest price medicines, order now and get free delivery", "spam"),
    ("Are we still meeting for the AI lab tomorrow?", "ham"),
    ("Please submit your lab report before Friday", "ham"),
    ("Can you share the notes of today's lecture?", "ham"),
    ("I will call you after the class ends", "ham"),
    ("The midterm exam schedule has been uploaded on LMS", "ham"),
    ("Let's have lunch at the cafeteria at 1 pm", "ham"),
    ("Mom asked you to bring groceries on the way home", "ham"),
    ("Our project meeting is moved to Monday morning", "ham"),
    ("Thanks for helping me with the Python assignment", "ham"),
    ("Is the 8-puzzle code working on your laptop?", "ham"),
]
texts, labels = zip(*messages)

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.3, random_state=0, stratify=labels)

vectorizer = CountVectorizer(lowercase=True, stop_words='english')   # bag of words
Xtr = vectorizer.fit_transform(X_train)
Xte = vectorizer.transform(X_test)

model = MultinomialNB(alpha=1.0)        # alpha = Laplace smoothing
model.fit(Xtr, y_train)
pred = model.predict(Xte)

print("Vocabulary size:", len(vectorizer.vocabulary_))
print("Test accuracy  :", accuracy_score(y_test, pred))
print(classification_report(y_test, pred, zero_division=0))

new = ["Click here to win a free laptop now",
       "Can we discuss the open ended lab project today?"]
for msg, p in zip(new, model.predict(vectorizer.transform(new))):
    print(f"{p.upper():5s} <- {msg}")
