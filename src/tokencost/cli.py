from tokencost.tokenizer import count_openai_tokens

def main():
    print("Token Cost Is Active Now...")
    token = count_openai_tokens("Hello World")  
    print("token -> ", token)