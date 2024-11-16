# AI Voice App using Google Text-to-Speech (gTTS)

from gtts import gTTS
import os

def text_to_speech():
    print("Welcome to the AI Voice App!")
    print("Type the text you want to convert to speech. (Type 'exit' to quit)")
    
    while True:
        user_input = input("\nEnter your text: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Convert text to speech
        tts = gTTS(text=user_input, lang='en')
        audio_file = "output.mp3"
        tts.save(audio_file)
        
        # Play the audio
        print(f"Playing audio for: '{user_input}'")
        os.system(f"start {audio_file}")  # For Windows
        # Use 'open' for macOS and 'xdg-open' for Linux if needed

# Run the app
if __name__ == "__main__":
    text_to_speech()