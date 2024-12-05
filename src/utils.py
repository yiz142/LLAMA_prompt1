# src/utils.py

def count_tokens(text):
    """Token counting using a simple string split method."""
    return len(text.split())

def truncate_text(text, max_tokens, reserve_tokens=50):
    """Truncate text to fit within a specified token budget."""
    tokens = text.split()
    max_input_tokens = max_tokens - reserve_tokens
    if len(tokens) > max_input_tokens:
        tokens = tokens[:max_input_tokens]
    return " ".join(tokens)

def estimate_cost(input_tokens, output_tokens, model_name):
    """Estimate the cost of model execution based on tokens."""
    cost_per_million = {
        'Meta-Llama-3.1-8B-Instruct': (0.10, 0.20),
        'Meta-Llama-3.2-1B-Instruct': (0.04, 0.08),
        'Meta-Llama-3.2-3B-Instruct': (0.08, 0.16),
    }
    input_price, output_price = cost_per_million.get(
        model_name, (0.10, 0.20)
    )
    total_input_cost = (input_tokens / 1e6) * input_price
    total_output_cost = (output_tokens / 1e6) * output_price
    return total_input_cost + total_output_cost
