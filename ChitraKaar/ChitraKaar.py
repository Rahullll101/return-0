#!pip install gradio torch diffusers transformers accelerate

import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

# Load the StableDiffusionPipeline model
pipe = StableDiffusionPipeline.from_pretrained("redstonehero/cetusmix_v4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
pipe.safety_checker = None

# Define the function that uses the StableDiffusionPipeline
def generate_image(prompt, h=800, w=640, steps=25, guidance=7.5):
    neg = "easynegative, human, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality..."

    image = pipe(prompt, height=h, width=w, num_inference_steps=steps,
                 guidance_scale=guidance,
                 negative_prompt=neg).images[0]
    return image

# Create a Gradio interface with live set to False
iface = gr.Interface(fn=generate_image,
                     inputs="text",
                     outputs="image",
                     live=False)

# Add a submit button
iface.launch(share=True)

# You can manually trigger the interface to submit using the following line:
# iface.launch()
