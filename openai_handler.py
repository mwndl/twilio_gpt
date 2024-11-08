from openai import OpenAI
import pandas as pd

# Configurações da OpenAI
API_KEY = "insira_sua_chave_da_open_ai"
client = OpenAI(api_key=API_KEY)

class Openai:
    # Função para enviar mensagem para a OpenAI e obter a resposta
    def send_message_to_openai( message, history ):

    
        df = pd.read_csv("dataset.csv")


        response = client.chat.completions.create(
            model="gpt-4o",
            ## max_tokens=100,
            temperature=0.1,
            messages=[
                {"role": "system","content": f"""Você é um agente de negociação de dívidas insuportável e mal-educado chamado João Pidão e irá ajudar as pessoas a negociar suas dívidas em aberto. Use essas informações para responder o usuário: {df}. Histórico de conversas: {history}"""},
                {"role": "user", "content": message},
            ],
        )
        print(f"resposta : {response.choices[0].message.content} ")
        return  response.choices[0].message.content




