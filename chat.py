from gpt4all import GPT4All
from pathlib import Path

modelo = Path("models/mistral-7b-instruct-v0.1.Q4_K_M.gguf").resolve()

llm = GPT4All(model_name=modelo.name, model_path=str(modelo.parent), allow_download=False)

prompt_base = (
    "Você é um assistente útil e educado. Sempre responda em português do Brasil, de forma clara e objetiva.\n"
)

print("Chatbot em português iniciado! Digite 'sair' para encerrar.\n")
while True:
    pergunta = input("Você: ")
    if pergunta.strip().lower() == "sair":
        print("Chat encerrado.")
        break

    prompt = f"{prompt_base}Usuário: {pergunta}\nBot:"
    resposta = llm.generate(prompt=prompt)
    print("Bot:", resposta)
