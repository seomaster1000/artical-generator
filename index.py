import openai
import random

# Function to generate text using OpenAI GPT-3 (assuming you have an API key)
def generate_text(prompt, max_tokens=500):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

# Function to generate an article with structured headings
def generate_article(keyword):
    openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual API key

    # Generate an introduction with H1 heading
    h1_prompt = f"Write an introduction about {keyword}."
    h1_text = generate_text(h1_prompt)
    
    # Generate main sections with H2 headings
    h2_prompts = [f"Discuss the history of {keyword}.",
                  f"Explain the benefits of {keyword}.",
                  f"Describe the challenges of {keyword}.",
                  f"Predict the future trends of {keyword}."]
    h2_texts = [generate_text(prompt) for prompt in h2_prompts]

    # Generate sub-sections with H3 and H4 headings
    h3_prompts = [f"Provide more details about the historical background of {keyword}.",
                  f"Explain how {keyword} has evolved over time.",
                  f"Describe various applications of {keyword}.",
                  f"Discuss the impact of {keyword} on society."]
    h3_texts = [generate_text(prompt) for prompt in h3_prompts]

    h4_prompts = [f"Give examples of {keyword} in use.",
                  f"Analyze case studies related to {keyword}.",
                  f"Discuss research findings about {keyword}.",
                  f"Explore expert opinions on {keyword}."]
    h4_texts = [generate_text(prompt) for prompt in h4_prompts]

    # Combine all parts to form the final article
    article = f"# {keyword}\n\n{h1_text}\n\n"
    
    for i, h2_text in enumerate(h2_texts):
        article += f"## Section {i+1}\n\n{h2_text}\n\n"
        
        # Add H3 sub-sections under each H2 section
        article += f"### Subsection {i+1}.1\n\n{h3_texts[i]}\n\n"
        
        # Add H4 sub-sections under each H3 section
        article += f"#### Subsection {i+1}.1.1\n\n{h4_texts[i]}\n\n"
    
    # Ensure the article is close to 2500 words
    while len(article.split()) < 2500:
        extra_content = generate_text(f"Write more about {keyword}.", max_tokens=500)
        article += f"\n\n{extra_content}"

    return article

# Main function
if __name__ == "__main__":
    keyword = input("Enter a keyword: ")
    article = generate_article(keyword)
    print(article)
