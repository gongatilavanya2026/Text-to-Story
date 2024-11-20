import streamlit as st
import cohere

api_key = "YOUR_COHERE_API_KEY"
co = cohere.Client(api_key)

def text_to_story(input_text):
    prompt = f"Create a detailed and creative story based on the following text: {input_text}"
    
    response = co.generate(
        model="large",  # Updated model
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        stop_sequences=["\n"]
    )
    
    return response.generations[0].text.strip()

# Example usage
input_text = "A young knight embarks on an adventure to find a hidden treasure."
story = text_to_story(input_text)
print(story)
