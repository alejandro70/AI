import openai
import os
import io

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

with io.open("security-report.txt",'r',encoding='utf8') as f:
    text_1 = f.read()
    
prompt = f"""
Se le proporcionará un texto delimitado por comillas triples. \
Este contiene el reporte de seguridad del software Modeler. \
Usted deberá mejorar la redacción y complementar la información técnica para comunicar este reporte al gerente de desarrollo de software.
\"\"\"{text_1}\"\"\"
"""

response = get_completion(prompt)
print(response)