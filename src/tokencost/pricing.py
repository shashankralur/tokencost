from dataclasses import dataclass

@dataclass(frozen=True)
class PriceEntry:
    provider: str
    model: str
    price_per_1000_tokens: float
    

PRICES = [
    PriceEntry(
        provider="openai",
        model="gpt-4o-mini",
        price_per_1000_tokens=0.00015
    ),
    PriceEntry(
        provider="anthropic",
        model="claude-3-5-haiku",
        price_per_1000_tokens=0.001
    ),
]

def estimate_cost(token_count:int, price:PriceEntry) -> float:
    estimated_cost = (token_count / 1000) * price.price_per_1000_tokens
    return estimated_cost