from tokencost.tokenizer import count_openai_tokens

def test_known_string():
    assert count_openai_tokens("Hello World") == 2
    
def test_empty_string():
    assert count_openai_tokens("") == 0
    
def test_very_long_string():
    text = "Hellow World" * 1000
    token_count = count_openai_tokens(text)
    
    assert token_count > 0