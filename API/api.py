from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json 
import pandas as pd

app = FastAPI()

class BaseInput(BaseModel):
    place_name : str

def recommender(place):
    print(new_df['name'])
    place_index = new_df[new_df['name']==place].index[0]
    distances = similarity[place_index]
    place_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]
    print(place_list)
    recommendation = [] 
    for i in place_list:
        recommendation.append(i)
    
    print(recommendation)
    return recommendation

new_df = pickle.load(open('new_df.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))
places = pd.DataFrame(new_df)


@app.post('/recommend')
def recommend(input_params:BaseInput):
    print(input_params)
    input_data = input_params.json()
    input_dict = json.loads(input_data)
    print(input_dict)
    place_name = input_dict['place_name']
    print(place_name)
    prediction = recommender(place_name)
    return prediction

