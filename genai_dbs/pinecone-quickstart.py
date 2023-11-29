#Code is from here: https://docs.pinecone.io/docs/quickstart
#NOTES:
## + Hard-coded data set for easy start
## + Embedding values are short (8 dimensions)
## + Does not require any external steps except pinecone account, instance, and key
## - No Github repo with example scripts for Hello World or Quickstart
## - Not helpful if you have a data set without embeddings

import pinecone

pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENVIRONMENT")

pinecone.create_index("quickstart", dimension=8, metric="euclidean")
pinecone.describe_index("quickstart")

index = pinecone.Index("quickstart")

index.upsert(
  vectors=[
    {"id": "A", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
    {"id": "B", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
    {"id": "C", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
    {"id": "D", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
    {"id": "E", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}
  ]
)

index.query(
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  top_k=3,
  include_values=True
)
# Returns:
# {'matches': [{'id': 'C',
#               'score': 0.0,
#               'values': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
#              {'id': 'D',
#               'score': 0.0799999237,
#               'values': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
#              {'id': 'B',
#               'score': 0.0800000429,
#               'values': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]}],
#  'namespace': ''}

pinecone.delete_index("quickstart")