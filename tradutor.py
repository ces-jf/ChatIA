#pip install deep-translator
from deep_translator import GoogleTranslator, MyMemoryTranslator, LingueeTranslator, PonsTranslator

def chatbot():
    print("Olá! Sou um chatbot de ")
    while True:
        texto = input("\nDigite o texto para traduzir: ")
        if texto.lower() == "sair":
            print("Até logo!")
            break
        idioma_destino = input("Para qual idioma você quer traduzir (ex: en, es, fr, de): ")
        try:
            traducao = GoogleTranslator(source='auto', target=idioma_destino).translate(texto)
            translated = MyMemoryTranslator(source='portuguese', target='english').translate(texto)
            translated_word = LingueeTranslator(source='portuguese', target='english').translate(texto)
            # translated_word2 = PonsTranslator(source='pt', target='en').translate(texto)
            print(f"Tradução: {traducao}")
            print(f"Tradução 2: {translated}")
            print(f"Tradução 3: {translated_word}")
            # print(f"Tradução 4: {translated_word2}")
        except Exception as e:
            print(f"Erro na tradução: {e}")

chatbot()
