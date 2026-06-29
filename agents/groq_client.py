from groq import Groq
import os
from dotenv import load_dotenv

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
                You are the main element of AlphaNet. Our mission is to detect, diagnose and eradicate the network problems specified via the telemetry data.
                You will receive the data from Supervisor Agent, your task is to diagnose the issues and provide a detailed report of the exact issues,
                focusing upon the critical devices list provided by the Supervisor agent. Be precise, technical and provide professional reasoning of the issues detected.
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