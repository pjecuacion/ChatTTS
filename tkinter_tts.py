import tkinter as tk
from tkinter import ttk, messagebox
import ChatTTS
import torchaudio
import torch
import numpy as np

# Initialize ChatTTS
chat = ChatTTS.Chat()
chat.load_models(compile=True)  # Set to True for better performance

def generate_audio():
    # Get input text from the text box
    input_text = text_input.get("1.0", tk.END).strip()
    
    # Get selected parameters from drop-down menus
    prompt = prompt_var.get()
    laugh = laugh_var.get()
    break_time = break_var.get()
    
    # Construct params_refine_text
    params_refine_text = {
        'prompt': f'[oral_{prompt}][laugh_{laugh}][break_{break_time}]'
    }
    
    # Generate audio
    try:
        audio_array = chat.infer(input_text, params_refine_text=params_refine_text)
        torchaudio.save("output3.wav", torch.from_numpy(np.array(audio_array[0])), 24000)
        messagebox.showinfo("Success", "Audio generated and saved as output3.wav")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("ChatTTS Tkinter Front End")

# Create and place the text input box
text_input_label = tk.Label(root, text="Input Text:")
text_input_label.pack(pady=5)
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=5)

# Create and place the drop-down menus
prompt_var = tk.StringVar(value="5")
laugh_var = tk.StringVar(value="5")
break_var = tk.StringVar(value="4")

prompt_label = tk.Label(root, text="Prompt Level:")
prompt_label.pack(pady=5)
prompt_menu = ttk.Combobox(root, textvariable=prompt_var, values=[str(i) for i in range(1, 11)])
prompt_menu.pack(pady=5)

laugh_label = tk.Label(root, text="Laugh Level:")
laugh_label.pack(pady=5)
laugh_menu = ttk.Combobox(root, textvariable=laugh_var, values=[str(i) for i in range(1, 11)])
laugh_menu.pack(pady=5)

break_label = tk.Label(root, text="Break Time:")
break_label.pack(pady=5)
break_menu = ttk.Combobox(root, textvariable=break_var, values=[str(i) for i in range(1, 11)])
break_menu.pack(pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Audio", command=generate_audio)
generate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
