# EXPLAIN: OpenAI + Gradio Image Generator

## What This Does

You type a description of an image (e.g., "A dog in a pirate hat"). The program sends that to OpenAI's DALL-E. DALL-E creates an image and returns a URL. Gradio shows it in a web interface.

---

## Step-by-Step

### 1. OpenAI Client
`OpenAI(api_key=...)` creates a client. The key comes from your environment variable `OPENAI_API_KEY`.

### 2. generate_image()
- Takes your text prompt and desired size
- Calls `client.images.generate()` with model "dall-e-2"
- Returns the URL of the generated image

### 3. Gradio Interface
`gr.Interface()` takes: your function, inputs (text box + radio for size), outputs (image). Gradio builds the form and displays the result.

### 4. launch()
Starts a local web server. You get a URL like http://127.0.0.1:7860. Open it in a browser.

---

## Setup

1. Set `OPENAI_API_KEY` in .env or environment
2. `pip install openai gradio`
3. Run `python image_generator.py`
