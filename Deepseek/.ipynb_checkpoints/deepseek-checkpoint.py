import json
from openai import OpenAI
with open ("zelaiHandi_berriak_ds_4.jsonl", "r") as file: #wikipedia
    berriak = json.load(file) 

client = OpenAI(api_key="sk-025aaf98e1cc4d8f8d79d76182096bd2", base_url="https://api.deepseek.com")

def sailkapena(txt, klasifikazioa):
    prompt = f"""
    Clasiffy the following Basque texts into one of these categories:{', '.join(klasifikazioa)}. Respond only with the category name. If the text does not fit any of the categories, classify it as "Other". Do not include explanations.
    Text: {txt!r}
    Category:
    """
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": "You are a text classifier in Euskera."},
            {"role": "user", "content": prompt}
        ],
        temperature= 1.3
    )
    return response.choices[0].message.content.strip()

klasifikazioa = [
    "Zientzia eta teknologia",
    "Ekonomia",
    "Politika",
    "Gizartea",
    "Geografia",
    "Historia",
    "Kirola"]

for berri in berriak:
    gaia = sailkapena(berri,klasifikazioa)
    tup = (berri,gaia)
    with open("berriak_sailkatuta_d_2.txt","a") as file:
        print(repr(tup), file=file)
