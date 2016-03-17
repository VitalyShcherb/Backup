from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/home/ubuntu/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz', path_to_jar='/home/ubuntu/stanford-ner-2015-12-09/stanford-ner.jar')
text = 'While in Frabce'

tokenized_text = word_tokenize(text)
#print tokenized_text
#classified_text = st.tag(tokenized_text)
#print(classified_text)




import nltk
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('/home/ubuntu/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz', path_to_jar='/home/ubuntu/stanford-ner-2015-12-09/stanford-ner.jar')
print st._stanford_jar
stanford_dir = st._stanford_jar.rpartition('/')[0]
from nltk.internals import find_jars_within_path
stanford_jars = find_jars_within_path(stanford_dir)
print ":".join(stanford_jars)
st._stanford_jar = ':'.join(stanford_jars)
print st._stanford_jar
text = st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
print text