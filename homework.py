# Product review analysis

# 1
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

search_term = input("Enter a search term: ")

def search_reviews(search_term):
    for sentence in reviews:
        if search_term in sentence:
            return True
            
print("Word available:", search_reviews(search_term))


# 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def sentiment_analysis(positive_words, negative_words):
    count_positive = 0
    count_negative = 0

    for word in positive_words:
        if search_reviews(word):
            count_positive += 1
            
    for word in negative_words:
        if search_reviews(word):
            count_negative += 1
            
    return count_positive, count_negative
    
positive, negative = sentiment_analysis(positive_words, negative_words)
print(f"Positive words: {positive} Negative words: {negative}")
        
        
# 3

count = 0
def review_summary(review):
    for sentence in review:
        if len(sentence) <= 30:
            print(sentence) 
        else:
            last_space = sentence[:30].rfind(" ")
            print(sentence[:last_space] + "...")
        
review_summary(reviews)
        