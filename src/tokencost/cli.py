from tokencost.tokenizer import count_openai_tokens
from tokencost.pricing import estimate_cost, PRICES

def main():
    text = "Hello World"
    token_count = count_openai_tokens(text)
    
    for price in PRICES:
        cost = estimate_cost(token_count, price)
        print(
            f"{price.provider:<11}"
            f"{price.model:<11}"
            f"{token_count:<9}"
            f"{cost:.6f}"
        )
        
if __name__ == "__main__":
    main()