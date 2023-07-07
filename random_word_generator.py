from random import randint


def pick_random_word():
    word_list = ["afforest", "consequences", "event", "especially", "catastrophic", "one", "cloud", "nine", "feel", "extreme", "happiness", "relation", "establish", "forest", "previously", "unforested", "land", "becalm",
                 "make", "still", "steady", "tranquil", "blithesome", "carefree", "and", "happy", "lighthearted", "broadsheet", "advertisement", "intended", "wide", "distribution", "buffoonish", "like", "clown", "caprice", "sudden",
                 "desire", "capricious", "determined", "chance", "impulse", "rather", "than", "necessity", "causerie", "light", "informal", "conversation", "social", "occasions", "chivalrous",
                 "attentive", "honorable", "like", "ideal", "knight", "forhead", "simplicity", "surprise", "accident", "cooking", "water", "mirror", "camphor", "utensil", "stainless"]
    selected_index = randint(0, len(word_list)-1)
    return word_list[selected_index]
