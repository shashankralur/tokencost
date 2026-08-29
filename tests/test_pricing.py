from tokencost.pricing import PriceEntry, estimate_cost

def test_cost_for_1000_tokens():
    price = PriceEntry(
        provider="test",
        model="test-model",
        price_per_1000_tokens=0.01,
    )
    
    assert estimate_cost(1000, price) == 0.01
    

def test_cost_for_500_tokens():
    price = PriceEntry(
        provider="test",
        model="test-model",
        price_per_1000_tokens=0.05
    )
    
    assert estimate_cost(500, price) == 0.025
    
def test_zero_tokens():
    price = PriceEntry(
        provider="test",
        model="test-model",
        price_per_1000_tokens=0.01
    )
    
    assert estimate_cost(0, price) == 0