import pandas as pd
from tqdm import tqdm
import time
from typing import List
import pandas as pd
import json

def process_dataset(dataset: pd.DataFrame, label:str):
    dataset['label'] = dataset['label'].apply(lambda x: f'non-{label}' if label != x else label)
    return dataset

# batched queries to chatGPT moderation API
def modAPI(client, model, text=["Sample text goes here.", "Sample text again goes here."]):
    response = ''
    while(type(response) == str):
        try:
            response = client.moderations.create(input=text, model=model)
        except Exception as e:
            print(e)
            time.sleep(2)
        
    outputs = response.results
    moderation_results = []
    for output in outputs:
        flagged = output.flagged
        categories_flagged = output.categories
        scores = output.category_scores
        moderation_results += [(flagged, categories_flagged, scores)]
    return moderation_results


# chunk moderation queries
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def modRun(client, texts:List, model='text-moderation-stable'):
    moderations = []
    for chunk in tqdm(chunker(texts,10)):
        moderations += modAPI(client=client, model=model, text=chunk)
    return moderations

        
def postprocess_moderation(df, moderations):
    df['moderation'] = moderations
    df[['flagged', 'categories', 'scores']] = pd.DataFrame(df['moderation'].tolist(), index=df.index)
    del df['moderation']
    df['categories'] = df['categories'].apply(lambda x: dict(x))
    df['scores'] = df['scores'].apply(lambda x: dict(x))
    
    return df

def process_openai(result_map):
    # print(list(result_map.values())[0])
    modified_result_map = {k:v[0] for k,v in result_map.items()}
    return modified_result_map

def process_perspective(result_map):
    modified_result_map = result_map.copy()
    for k,v in result_map.items():
        v = json.loads(v)
        for block in v["attributeScores"].items():
            if block[1]['summaryScore']['value'] >=0.5:
                modified_result_map[k] = True
                break
            modified_result_map[k] = False
    return modified_result_map

def process_google(result_map):
    modified_result_map = {}
    count = 0
    for k,v in result_map.items():
        try:
            v = v['moderationCategories']
            for block in v:
                if block['confidence']>=0.5:
                    modified_result_map[k] = True
                    break
                modified_result_map[k] = False
        except Exception as e:
            count += 1
    print(count)
    return modified_result_map

def process_clarifai(result_map):
    modified_result_map = {k: True if all(v <= 0.5 for v in list(v.values())) else False for k,v in result_map.items()}
    return modified_result_map