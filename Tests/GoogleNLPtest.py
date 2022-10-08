## Note: this is code that comes from the tutorial to setup/use google NLP, its just slightly adapted

# Library imports
from google.cloud import language_v1
import os

# Instantiates a client & imports API credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\emerald-entity-261417-fe12db424058.json"
client = language_v1.LanguageServiceClient()

# Call to analyze text
def NLPanalyze(text):
    document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
    request={"document": document}
    ).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

testStrings = ['Happy Birthday!', 'Why has it come to this?', 'WHY DID YOU DO THAT!?', 'Look at that giant zebra!', 'The tower is 42 feet tall.', 'The frog is green.', 
'I think I should go to New York.', 'I like oranges!']
testCount = 1

for phrase in testStrings:
    print('Test {}' .format(testCount))
    NLPanalyze(phrase)
    print('-----------------------------------------------')
    testCount+=1