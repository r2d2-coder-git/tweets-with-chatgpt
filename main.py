import openai
import tweepy
import tkinter as tk
import sys
tweet_text = ""
question_chat_gpt = ""


def on_submit_click_question():
    # función llamada cuando se hace clic en el botón Enviar
    global question_chat_gpt
    question_chat_gpt = entry_question.get()
    root_question.destroy()
    
    
def on_submit_click_answer():
    # función llamada cuando se hace clic en el botón Enviar
    global tweet_text
    tweet_text = entry_answer.get("1.0","end")
    root_answer.destroy()  

def on_submit_cancel():
      root_answer.destroy()
      sys.exit()
############################################ CREAR VENTANA PARA CREAR PREGUNTA CHATGPT ######################################

# Crear una ventana
root_question = tk.Tk()
root_question.title("Pregunta")
root_question.geometry("400x200")

# Crear una etiqueta con la pregunta
question = tk.Label(root_question, text="Sobre que quieres twittear?:")
question.pack()

# Crear un campo de texto para la respuesta
entry_question = tk.Entry(root_question)
entry_question.pack()
entry_question.insert(0, "Texto por defecto")

# Crear un botón Enviar
submit_button = tk.Button(root_question, text="Enviar", command=on_submit_click_question)
submit_button.pack()
# Ejecutar la ventana
root_question.mainloop()

############################################ CONSEGUIR RESPUESTA CHATGPT ######################################

# Set your API key
openai.api_key = "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"

# Generate a response from the API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question_chat_gpt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
tweet_text = response["choices"][0]["text"]

############################################ CREAR VENTANA CON TEXTO DE CHATGPT ######################################

# Crear una ventana
root_answer = tk.Tk()
root_answer.title("Respuesta ChatGPT")
root_answer.geometry("500x300")

# Crear una etiqueta con la pregunta
question = tk.Label(root_answer, text="Escribe algo:")
question.pack()

# Crear un campo de texto para la respuesta
entry_answer = tk.Text(root_answer, height=10, width=40)
entry_answer.pack()
entry_answer.insert("1.0",tweet_text )

# Crear un botón Enviar
submit_button = tk.Button(root_answer, text="Enviar", command=on_submit_click_answer)
submit_button.pack()
cancel_tweet = tk.Button(root_answer, text="Cancelar", command=on_submit_cancel)
cancel_tweet.pack()
# Ejecutar la ventana
print(len(tweet_text))
root_answer.mainloop()



############################################ SUBIR TWEET ######################################

# Set up your Twitter API credentials
consumer_key = "NYc06VF2urm6kYPhxIIJC6ZoY"
consumer_secret = "hTDgEHTsZgQfhqJnYVurO9raYfn1qyaFm2zTwKQnlJzO8HjKpm"
access_token = "1605983645931634690-NXmhKDVYJufladIjDF1pXxkEyR7Jd4"
access_token_secret = "NYJnRXmNfqaukb8x0BX0wtCjxkSFeUvCXwwdPKsPOAsXb"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAbblgEAAAAAIAQb4vHo0WR2l9yUdDv4sIHjS10%3D04PvyMVlFaYor41oVR4GA0ssLwwia9vUo7XXN9Z69xOMHSFEGZ'
if len(tweet_text) <= 280:
    client = tweepy.Client(bearer_token=bearer_token,consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)

    client.create_tweet(text = tweet_text)
else:
    print("Tu tweet es demasiado largo")


