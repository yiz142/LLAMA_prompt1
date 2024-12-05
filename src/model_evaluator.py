# src/model_evaluator.py

import random
import time
from src.prompting_methods import (
    direct_prompt, chain_of_thought_prompt, few_shot_prompt
)
from src.utils import count_tokens, truncate_text, estimate_cost
from src.api_client import get_completion

def evaluate_model(
    data, classes, model_name, prompting_method,
    num_samples_per_class=10, token_budget=4000, delay=2, max_retries=3
):
    """Evaluate a model with a specific prompting method."""
    correct_predictions = 0
    total_cost = 0
    total_samples = 0
    classes_formatted = ", ".join(classes)

    selected_data = select_samples(data, num_samples_per_class)

    for cls, samples in selected_data.items():
        for item in samples:
            text = truncate_text(item['text'], token_budget, reserve_tokens=100)

            if prompting_method == 'direct':
                prompt = direct_prompt(text, classes_formatted)
            elif prompting_method == 'chain-of-thought':
                prompt = chain_of_thought_prompt(text, classes_formatted)
            elif prompting_method == 'few-shot':
                examples = random.sample(data, min(3, len(data)))
                examples = [(ex['text'], ex['class']) for ex in examples]
                prompt = few_shot_prompt(text, examples, classes_formatted)
            else:
                raise ValueError(f"Unknown prompting method: {prompting_method}")

            input_token_count = count_tokens(prompt)
            if input_token_count > token_budget:
                print(f"Skipping sample due to token limit: {input_token_count} tokens")
                continue

            retries = 0
            while retries <= max_retries:
                try:
                    response_text = get_completion(prompt, model_name)
                    output_token_count = count_tokens(response_text)
                    total_cost += estimate_cost(
                        input_token_count, output_token_count, model_name
                    )
                    if response_text.strip().lower() == cls.lower():
                        correct_predictions += 1
                    break  # Exit retry loop on success
                except Exception as e:
                    print(f"Error: {e}")
                    retries += 1
                    time.sleep(delay)
            total_samples += 1

    accuracy = correct_predictions / total_samples if total_samples > 0 else 0
    return accuracy, total_cost

def select_samples(data, num_samples_per_class=10):
    classes = set(item['class'] for item in data)
    selected_data = {cls: [] for cls in classes}

    for item in data:
        if len(selected_data[item['class']]) < num_samples_per_class:
            selected_data[item['class']].append(item)
    return selected_data
