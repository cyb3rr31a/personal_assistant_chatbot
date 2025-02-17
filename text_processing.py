import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def clean_text(user_message):
  """Process and clean user input text"""
  doc = nlp(user_message.lower()) # Convert to lowercase

  # Remove stopwords and punctuation
  filtered_words = [token.text for token in doc if not token.is_stop and not token.is_punct]

  return " ".join(filtered_words)

# Example Usage
if __name__ == "__main__"
  user_message = "Hey!! Can you tell me the weather in New york?" # Change to accept input
  processed_text = clean_text(user_message)
  print("Processed Text:", processed_text)
