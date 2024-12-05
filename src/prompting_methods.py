# src/prompting_methods.py

def direct_prompt(text, classes_formatted):
    return (
        f"{text}\n\n"
        f"Classify the above text into one of the following categories: "
        f"{classes_formatted}.\nProvide only the category name as your answer."
    )

def chain_of_thought_prompt(text, classes_formatted):
    return (
        f"{text}\n\n"
        f"Think step by step to classify the above text into one of the "
        f"following categories: {classes_formatted}.\n"
        f"Provide only the category name as your answer."
    )

def few_shot_prompt(text, examples, classes_formatted):
    examples_text = "\n".join(
        [f"Text: {ex[0]}\nLabel: {ex[1]}" for ex in examples]
    )
    return (
        f"{examples_text}\n\nNow, classify the following text:\n"
        f"Text: {text}\n\nChoose the category from the following options: "
        f"{classes_formatted}.\nProvide only the category name as your answer."
    )
