reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def keyword(reviews):
    edited_reviews = []
    for review in reviews:
        if "good" in review:
            upper_good = review.replace("good", "GOOD")
            edited_reviews.append(upper_good)
        elif "excellent" in review:
            upper_excellent = review.replace("excellent", "EXCELLENT")
            edited_reviews.append(upper_excellent)
        elif "bad" in review:
            upper_bad = review.replace("bad", "BAD")
            edited_reviews.append(upper_bad)
        elif "poor" in review:
            upper_poor = review.replace("poor", "POOR")
            edited_reviews.append(upper_poor)
        elif "average" in review:
            upper_average = review.replace("average", "AVERAGE")
            edited_reviews.append(upper_average)
        else:
            continue
    return edited_reviews   
            
print(keyword(reviews))

#Task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def count_reviews_with_positive_words(reviews, positive_words):
    positive_count = 0
    for review in reviews:
        if any(word in review.lower() for word in positive_words):
            positive_count += 1
    return positive_count

def count_reviews_with_negative_words(reviews, negative_words):
    negative_count = 0
    for review in reviews:
        if any(word in review.lower() for word in negative_words):
            negative_count += 1
    return negative_count

print(count_reviews_with_positive_words(reviews, positive_words)) 
print(count_reviews_with_negative_words(reviews, negative_words))

#Task 3

def abridged_reviews(reviews):
    abridged = []
    for review in reviews:
        if len(review) > 30:
            abridged.append(review[:31] + "...")
        else:
            abridged.append(review)
    return abridged

print(abridged_reviews(reviews))  