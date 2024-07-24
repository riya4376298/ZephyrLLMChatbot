import gradio as gr
from huggingface_hub import InferenceClient

"""
For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")



def respond(
    message,
    history: list[tuple[str, str]],
    temperature,
    top_p,
):
    system_message = "🌍 Welcome to the Language Learning Buddy! 🌍\n\nI'm here to assist you in learning languages. Whether you want to practice vocabulary, improve pronunciation, or learn about cultural nuances, I'm your guide. Feel free to ask me questions or start a language lesson!"



    messages = [{"role": "system", "content": system_message}]


    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})


    messages.append({"role": "user", "content": message})

    response = ""


    for message in client.chat_completion(
        messages,
        max_tokens=max_tokens,
        response += token
        yield response

"""
For information on how to customize the ChatInterface, peruse the gradio docs: https://www.gradio.app/docs/chatinterface
"""

demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="🌍 Welcome to the Language Learning Buddy! 🌍\n\nI'm here to assist you in learning languages. Whether you want to practice vocabulary, improve pronunciation, or learn about cultural nuances, I'm your guide. Feel free to ask me questions or start a language lesson!", label="System Message", lines=4),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Maximum Tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            label="Top-p (Nucleus Sampling)",
        ),
    ],

    examples=[
        ["How do you say 'hello' in Spanish? 🇪🇸"],
        ["Can you teach me some basic French phrases? 🇫🇷"],
        ["What are the tones in Mandarin Chinese? 🇨🇳"],
    ],
    title='Language Learning Buddy 🌍',
    description='''<div style="text-align: right; font-family: Arial, sans-serif; color: #333;">
                   <h2>Welcome to the Language Learning Buddy 🌍</h2>
                   <p style="font-size: 16px; text-align: right;">I'm here to assist you in learning languages. Whether you want to practice vocabulary, improve pronunciation, or learn about cultural nuances, I'm your guide.</p>
                   <p style="text-align: right;"><strong>Examples:</strong></p>
                   <ul style="list-style-type: disc; margin-left: 20px; text-align: right;">
                       <li style="font-size: 14px;">How do you say 'hello' in Spanish? 🇪🇸</li>
                       <li style="font-size: 14px;">Can you teach me some basic French phrases? 🇫🇷</li>
                       <li style="font-size: 14px;">What are the tones in Mandarin Chinese? 🇨🇳</li>
                   </ul>
                   </div>''',
)


if __name__ == "__main__":
    demo.launch()
