################################################################################
# In the given code, spaCy library is used to load the pre-trained English language model('en_core_web_sm') and also three words' cat',' monkey', and' banana' are reused using this model.
# #The' similarity' function of the spaCy library is also used to calculate the similarity between these words.
# Interestingly, the similarity scores between' cat' and' monkey' and between' banana' and' cat' are fairly low(0.56 and0.5, independently), whereas the similarity between' banana' and' monkey' is relatively high(0.76).
# This is because' cat' and' monkey' are two different creatures that don't partake numerous features or characteristics, whereas' banana' and' monkey' are both objects from the same terrain, and therefore partake some parallels.
# The law also goes on to calculate the pairwise similarity between commemorates of the judgment ' cat monkey banana'.
# As anticipated, the similarity score between' cat' and' monkey' and between' banana' and' monkey' is advanced than between' cat' and' banana'.
# Incipiently, the law compares the similarity between the given judgment ' Why is my cat on the auto' and a list of other rulings.
# The spaCy library is used to reuse each judgment , and the' similarity' function is used to calculate the similarity between each judgment and the given judgment .
# Overall, the intriguing observation about the similarity between' cat',' monkey', and' banana' highlights the fact that similarity measures depend on the environment and the task at hand.
# While' banana' and' monkey' are analogous in some surrounds,' cat' and' monkey' are not, and the similarity scores reflect this difference.
##########################################################################################


import spacy
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word1))
print(word3.similarity(word2))

tokens = nlp('cat monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go?",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)
