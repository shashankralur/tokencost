# tokencost

A small CLI tool that estimates LLM prompt token count and cost —
built as a learning project to prove out a real Python packaging
pipeline (src layout, setuptools, editable installs) before tackling
a larger package series.

> **Status:** learning/warm-up project. Feature-complete for its
> intended scope — token counting and cost estimation wired together,
> with pricing sourced from a user-editable file rather than
> hardcoded in code. Not published to PyPI; intentionally kept as a
> GitHub-only reference project. Accepting arbitrary CLI text/file
> input was scoped as a possible next step and isn't included here.

## Why this exists

Two goals: prove the packaging mechanism (folder structure →
`pyproject.toml` → editable install → real terminal command) end to
end, and avoid the common mistake of silently guessing at pricing —
if a model's price isn't known, this tool should say so clearly
rather than assume a number.

## Install

```bash
git clone https://github.com/<your-username>/tokencost.git
cd tokencost
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Usage

```bash
tokencost
```

Counts tokens for the example prompt using `tiktoken`, looks up the
price per model from `pricing.json`, and prints the estimated cost.

## Pricing

Prices are **not hardcoded** in the source code. They live in
`pricing.json`, which you can edit directly:

```json
{
  "gpt-4o": {
    "input_per_1k": 0.0050,
    "output_per_1k": 0.0150
  }
}
```

If a model isn't listed in this file, the tool won't guess a price —
it reports that the model is unknown rather than silently assuming a
number.

## How it works

- **Token counting** — `tiktoken`, OpenAI's own tokenizer library,
  gives an exact count rather than a word-split approximation.
- **Pricing** — read from `pricing.json` at runtime, kept separate
  from the counting logic so each piece is independently testable.
- **Packaging** — src layout with `setuptools`; see `pyproject.toml`
  for the entry point that turns this into the `tokencost` command.

## Running tests

```bash
pip install pytest
pytest
```

## Possible next steps (not built here)

- Accept arbitrary text via CLI argument or `--file`, instead of a
  fixed example prompt
- Support additional providers (Anthropic, Google) with their own
  approximate token-counting logic
- CLI flags to override a price for a single run

## License

MIT