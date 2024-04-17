
import string  # straight up learnt  about this concept  through chatgpt, i figured it would be cleaner to just strip the punctuation instead of making a function that detects if theres a period at the end, but if you want me to redo it that way i can

                


#i now see that i forgot to  code the part where it replaces the key words with caps. but now  i already saw you do it on preclass which is a shame. Ill take the L like a man though

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


review_words = ["good", "excellent", "bad", "poor", "average"]




for review in reviews:
    words = review.split()
    for word in words:
        word_cleaned = word.strip(string.punctuation)  # method learnt by chatgpt to remove punctuation
        if word_cleaned.lower() in review_words:
            print(word_cleaned.upper())







positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def count_words(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
            word = word.strip(string.punctuation)
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1

    return positive_count, negative_count

positive_count, negative_count = count_words(reviews, positive_words, negative_words) 

print("Number of positive words:", positive_count)
print("Number of negative words:", negative_count)






review = "this product sucks, its absolute trash, dont ever buy this, Buying this product is the worst decision i have ever made in my life, i absolutely hate it. i would never buy it again. never ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever ever buy it again"

lastspace = review[:30].rfind(' ')
formated = review[:lastspace] if lastspace != -1 else review[:30]

print(formated, "... [read more]")
