import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Remove rows with empty 'textTranslated'
dataframe = dataframe.dropna(subset=['textTranslated'])

# Reset the index after removing rows
dataframe = dataframe.reset_index(drop=True)

#filtrage des emojis sur la colonne 'commentaires'
def filtrer_emojis(textTranslated):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symboles & pictogrammes
                           u"\U0001F680-\U0001F6FF"  # transports & symboles de voyage
                           u"\U0001F1E0-\U0001F1FF"  # drapeaux (indicateurs de pays)
                           u"\U00002702-\U000027B0"  # formes & symboles divers
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
    texte_filtre = re.sub(emoji_pattern, '', str(textTranslated))
    return texte_filtre

# Appliquer le filtrage des emojis sur la colonne 'textTranslated' et créer une nouvelle colonne 'commentaires'
dataframe['commentaires'] = dataframe['textTranslated'].apply(filtrer_emojis)

# Instancier le tokenizer et le modèle
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Fonction pour calculer le sentiment
def calculate_sentiment(text):
    tokens = tokenizer.encode(text, return_tensors='pt')
    result = model(tokens)
    sentiment = int(torch.argmax(result.logits))+1
    return sentiment

# Appliquer la fonction calculate_sentiment à la colonne 'textTranslated'
dataframe['sentiment'] = dataframe['commentaires'].astype(str).apply(calculate_sentiment)
