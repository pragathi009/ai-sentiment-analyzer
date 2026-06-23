positive_words = ["good", "great", "happy", "awesome", "excellent"]
negative_words = ["bad", "sad", "terrible", "awful", "poor"]

text = input("Enter a sentence: ").lower()

positive_score = sum(word in text for word in positive_words)
negative_score = sum(word in text for word in negative_words)

if positive_score > negative_score:
    print("Sentiment: Positive 😊")
elif negative_score > positive_score:
    print("Sentiment: Negative 😔")
else:
    print("Sentiment: Neutral 😐")