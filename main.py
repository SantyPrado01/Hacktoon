import openai
import pandas as pd

# Configura tu clave de API de OpenAI
openai.api_key = ''

# Función para analizar el sentimiento de una frase utilizando ChatGPT
def analizar_sentimiento(frase):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Modelo de lenguaje ChatGPT a utilizar
        prompt=frase,
        max_tokens=1,  # Limitar la respuesta a un solo token
        temperature=0,  # Desactivar la aleatoriedad en la generación de respuestas
        n=1  # Generar una sola respuesta
    )
    respuesta = response.choices[0].text.strip()
    return respuesta

# Obtener el texto del usuario
texto_usuario = input("Ingrese un texto: ")

# Analizar el sentimiento del texto
sentimiento = analizar_sentimiento(texto_usuario)

# Crear la tabla con la frase y la puntuación del sentimiento
data = {'Frase': [texto_usuario], 'Puntuación de Sentimiento': [sentimiento]}
df = pd.DataFrame(data)

# Imprimir la tabla
print(df)
