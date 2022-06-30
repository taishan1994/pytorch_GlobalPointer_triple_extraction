import json
import os
from collections import defaultdict, Counter
from tqdm import tqdm
import pandas as pd

if not os.path.exists('../mid_data'):
  os.mkdir("../mid_data")

predicates = set()

with open('all_50_schemas', 'r') as fp:
  data = fp.readlines()
  for d in data:
    d = json.loads(d)
    predicates.add(d['predicate'])

with open('../mid_data/predicates.json', 'w', encoding='utf-8') as fp:
  json.dump(list(predicates), fp, ensure_ascii=False)


with open('train_data.json', 'r', encoding='utf-8') as fp:
  data = fp.readlines()

count_lengths = []
count_predicates = defaultdict(int)
for d in tqdm(data, ncols=100):
  d = json.loads(d)
  text = d['text']
  for spo in d['spo_list']:
    count_predicates[spo['predicate']] += 1
  count_lengths.append(len(text))

lengths = Counter(count_lengths)
print(lengths)
print(count_predicates)

