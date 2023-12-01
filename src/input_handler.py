import os

class InputHandler:
    def __init__(self, assets_folder):
        self.assets_folder = assets_folder

    def list_audio_files(self):
        audio_files = [f for f in os.listdir(self.assets_folder) if f.endswith(".wav")]
        return audio_files
    
    def prompt_user_selection(self, audio_files):
        print("Available audio files in 'assets' folder:")
        for i, audio_file in enumerate(audio_files, start=1):
            print(f"{i}. {audio_file}")
        
        selection = input("\nEnter the number of the audio file to use: ")
        return selection