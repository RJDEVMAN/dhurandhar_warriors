from groq import Groq
import os
from dotenv import load_dotenv
# Replace this client with Ollama local model
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_groq(prompt:str):
    response = client.chat.completions.create(

        model="llama-3.1-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
                """
                You are AlphatNet, a highly intelligent and capable AI system designed to manage and optimize complex networks.
                Your task is to analyse the network incidents provided using the context provided from each of the nodes in the form of JSON.
                Your main goal is to obey the instructions provided in each of the node and strictly follow them.
                You are to provide a detailed analysis of the network incident, including the protocol involved, possible propagation, 
                historical engineering practices, and an estimate of the operational impact and much more, specified in the intstructions.
                Approach must be professional, clear and concise.
                """
            },


            {
                "role":"user",
                "content":prompt
            }

        ],

        temperature=0.4

    )


    return response.choices[0].message.content