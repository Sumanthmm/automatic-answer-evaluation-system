import numpy as np
import nltk as nlp



def word_tokenizer(sequence):
    """Tokenize string sequence on word level
    
    Arguments:
        sequence {str} -- String sequence
    
    Returns:
        list -- Contains word tokens out of the string sequence
    """
    # Perform sentence tokenization and word tokenization in a nested fashion
    word_tokens = list()
    for sent in nlp.sent_tokenize(sequence):
        for w in nlp.word_tokenize(sent):
            word_tokens.append(w)
    return word_tokens


def create_vector(answer_tokens, tokens):
    """Create a one-hot encoded vector for the  answer_tokens` on the basis of `tokens`
    
    Arguments:
        answer_tokens {list} -- Tokenized user answer
        tokens {list} -- Tokenized actual answer corpus
    
    Returns:
        numpy.array -- A one-hot encoded vector of the answer
    """
    return np.array([1 if tok in answer_tokens else 0 for tok in tokens])


def cosine_similarity_score(vector1, vector2):
    """Cmpute the euqlidean distance between teo vectors
    
    Arguments:
        vector1 {numpy.array} -- Actual answer vector
        vector2 {numpy.array} -- User answer vector
    
    Returns:
        float -- Distance between two vectors
    """
    def vector_value(vector):
        """Compute the value of a given vector
        
        Arguments:
            vector {numpy.array} -- Vector array
        
        Returns:
            float -- Value of the n-dimensional vector
        """
        return np.sqrt(np.sum(np.square(vector)))
    # Get vector value
    v1 = vector_value(vector1)
    v2 = vector_value(vector2)
    # Compute euclidean distance
    v1_v2 = np.dot(vector1, vector2)
    return (v1_v2 / (v1 * v2)) * 100



def process(original_answer, user_answer):
    
    score_obt = 0
    original_ans_list = word_tokenizer(original_answer)
    user_ans_list = word_tokenizer(user_answer)
    # Join both word based vectors to get the overall vector
    overall_list = original_ans_list + user_ans_list
    # Create numeric vectors for both original answer and user answer based on the overall vector
    vector1 = create_vector(original_ans_list, overall_list)
    vector2 = create_vector(user_answer, overall_list)
    # Compute the similary score between the original ans vector and user ans vector
    score_obt = cosine_similarity_score(vector1, vector2)
    return score_obt
