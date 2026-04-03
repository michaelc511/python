"""
Creating Designs by Leveraging OpenAI and Gradio UI
Generate images from text prompts using OpenAI's DALL-E API.
"""

import os
from openai import OpenAI
import gradio as gr

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_image(prompt, size="1024x1024"):
    """Call OpenAI DALL-E to create an image from the prompt."""
    if not prompt.strip():
        return None
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size=size,
        n=1,
    )
    image_url = response.data[0].url
    return image_url


def main():
    demo = gr.Interface(
        fn=generate_image,
        inputs=[
            gr.Textbox(
                label="Describe your image",
                placeholder="A serene mountain landscape at sunset with a lake...",
                lines=3,
            ),
            gr.Radio(
                choices=["1024x1024", "512x512", "1024x1792", "1792x1024"],
                value="1024x1024",
                label="Image size",
            ),
        ],
        outputs=gr.Image(label="Generated image"),
        title="AI Image Generator",
        description="Enter a prompt and OpenAI's DALL-E will create an image. Example: 'A cute cat wearing a spacesuit on Mars'",
    )
    demo.launch()


if __name__ == "__main__":
    main()
