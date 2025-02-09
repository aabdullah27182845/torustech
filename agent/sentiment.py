'''from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis")
tokenizer = AutoTokenizer.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis")


nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

sentences = ["$DOGE TO THE MOON!", "$TORUS is a scam", "Operating profit rose to EUR 13.1 mn from EUR 8.7 mn in the corresponding period in 2007 representing 7.7 percent of net sales.", "Bids or offers include at least 1,000 shares and the value of the shares must correspond to at least EUR 4,000.", "Raute reported a loss per share of EUR 0.86 for the first half of 2009 , against EPS of EUR 0.74 in the corresponding period of 2008."]
results = nlp(sentences)
for result in results:
    print(result)'''
    
from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=64, truncation=True, padding = 'max_length')
# post_1 & post_3 = bullish, post_2 = bearish
posts = [
    "See y'all tomorrow and can't wait to see ADA in the morning. I wonder what price it is going to be at. 😎🐂🤠💯😴 Bitcoin is looking good. Go for it and flash by that 45k.",
    "Alright racers, it’s a race to the bottom! Good luck today and remember there are no losers (minus those who invested in currency nobody really uses). Take your marks... Are you ready? Go!!",
    "I'm never selling. The whole market can bottom out. I'll continue to hold this dumpster fire until the day I die if I need to.",
    "$DOGE TO THE MOON!",
    "$DOGE scam as hell"
]

# Get predictions
predictions = pipe(posts)

def adjust_low_confidence_predictions(predictions, threshold=0.5):
    """
    Flips sentiment labels for predictions with confidence scores below the threshold.
    
    Args:
        predictions (list): List of dictionaries containing sentiment predictions.
                          Each dict should have 'label' and 'score' keys.
        threshold (float): Confidence threshold below which labels will be flipped.
                         Defaults to 0.5.
    
    Returns:
        list: List of dictionaries with adjusted predictions, containing:
              - original_label: The initial prediction label
              - score: The confidence score
              - final_label: The potentially flipped label
    """
    adjusted_predictions = []
    
    for pred in predictions:
        result = {
            'original_label': pred['label'],
            'score': pred['score'],
            'final_label': pred['label']
        }
        
        # Flip label if confidence is below threshold
        if pred['score'] < threshold:
            result['final_label'] = 'Bearish' if pred['label'] == 'Bullish' else 'Bullish'
            
        adjusted_predictions.append(result)
    
    return adjusted_predictions
predictions = adjust_low_confidence_predictions(predictions)

# Print the predictions
print(predictions)
    