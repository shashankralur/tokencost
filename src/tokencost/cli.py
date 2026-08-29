import argparse
import sys
from pathlib import Path

from tokencost.tokenizer import count_openai_tokens
from tokencost.pricing import estimate_cost, PRICES

def parse_args():
    parser = argparse.ArgumentParser(description="Estimate token usage and cost.")
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to count tokens for"
    )
    
    parser.add_argument(
        "--file",
        type=str,
        help="File to read text from"
    )
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.text is None and args.file is None:
        print("Error: provide text or use --file <path>.", file=sys.stderr)
        sys.exit(1)
    
    if args.text is not None and args.file is not None:
        print("Error: provide either text or --file, not both.", file=sys.stderr)
        sys.exit(1)
        
    if args.file is not None:
        path = Path(args.file)
        
        try:
            text = path.read_text()
        except FileNotFoundError:
            print(f"Error: file not found: {path}", file=sys.stderr)
            sys.exit(1)
    else:
        text = args.text
        
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