import re

class PromptOptimizer:
    def __init__(self):
        self.criteria = ["clarity", "specificity", "structure"]

    def evaluate_prompt(self, prompt):
        score = 0
        feedback = []

        # Check clarity (length & readability)
        if len(prompt.split()) > 8:
            score += 1
        else:
            feedback.append("Prompt is too short, add more details.")

        # Check specificity (keywords)
        keywords = ["how", "why", "explain", "steps", "guide"]
        if any(word in prompt.lower() for word in keywords):
            score += 1
        else:
            feedback.append("Add specific instructions like 'explain' or 'steps'.")

        # Check structure (punctuation / format)
        if prompt.endswith("?") or ":" in prompt:
            score += 1
        else:
            feedback.append("Improve structure using questions or formatting.")

        return score, feedback

    def optimize_prompt(self, prompt):
        optimized = f"""
Act as an expert in the relevant domain.

Task:
{prompt}

Instructions:
- Provide a detailed and structured response
- Use bullet points or steps where necessary
- Keep explanation clear and beginner-friendly

Output Format:
- Introduction
- Key Explanation
- Examples (if applicable)
- Summary
"""
        return optimized.strip()

    def suggest_improvements(self, feedback):
        if not feedback:
            return "Your prompt is already well-structured!"
        return "\n".join(feedback)


def main():
    print("=== SmartPrompt Optimizer ===")
    user_prompt = input("Enter your prompt: ")

    optimizer = PromptOptimizer()

    score, feedback = optimizer.evaluate_prompt(user_prompt)
    optimized_prompt = optimizer.optimize_prompt(user_prompt)

    print("\n--- Prompt Score ---")
    print(f"Score: {score}/3")

    print("\n--- Suggestions ---")
    print(optimizer.suggest_improvements(feedback))

    print("\n--- Optimized Prompt ---")
    print(optimized_prompt)


if __name__ == "__main__":
    main()