#from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


#with open('hyperskill-dataset-43723233.txt', 'r') as dataset:
    #vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True, analyzer='word', ngram_range=(1, 1), stop_words=None)
    #tfidf_matrix = vectorizer.fit_transform([dataset])
    
array = np.linspace(20, 42, num=11)
print(array[4])