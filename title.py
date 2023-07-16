import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import yake

# Download required NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

def get_heading(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Remove stop words from sentences
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [sentence for sentence in sentences if sentence.lower() not in stop_words]
    
    # Extract keywords from the text
    custom_kw_extractor = yake.KeywordExtractor()
    keywords = custom_kw_extractor.extract_keywords('. '.join(filtered_sentences))
    
    # Select the top-ranked keyword as the heading
    heading = keywords[0][0] if keywords else ""
    
    return heading
