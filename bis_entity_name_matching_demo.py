from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / 'bis_entity_preview_50.csv', encoding='utf-8-sig').fillna('')
assert 'Entity Name' in data.columns
names = data['Entity Name'].astype(str)
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4), lowercase=True)
X = vectorizer.fit_transform(names)
model = NearestNeighbors(metric='cosine', algorithm='brute').fit(X)
query = 'Chinese Academy of Sciences Institute of Physics'  # punctuation variation of preview name
q = vectorizer.transform([query])
distances, indices = model.kneighbors(q, n_neighbors=min(6, len(data)))
results = data.iloc[indices[0]].copy()
results.insert(0, 'Query', query)
results.insert(1, 'Text Similarity Score', (1 - distances[0]).round(4))
results.to_csv(HERE / 'bis_entity_name_matching_results.csv', index=False)
print(results[['Query', 'Entity Name', 'Country', 'Text Similarity Score']].to_string(index=False))
