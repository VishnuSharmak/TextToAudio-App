from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import pyttsx3
import os, time

class TextToAudio(App):
    def build(self):
        self.audio_file = None

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.text = TextInput(
            hint_text="Enter text here",
            size_hint=(1, 0.4)
        )

        self.voice = Spinner(
            text="English",
            values=("English", "Male", "Female", "Hindi"),
            size_hint=(1, 0.1)
        )

        btn_generate = Button(text="Generate Audio")
        btn_preview = Button(text="Preview Audio")
        btn_save = Button(text="Save Audio")

        btn_generate.bind(on_press=self.generate)
        btn_preview.bind(on_press=self.preview)
        btn_save.bind(on_press=self.save)

        layout.add_widget(Label(text="Offline Text To Audio", font_size=22))
        layout.add_widget(self.text)
        layout.add_widget(self.voice)
        layout.add_widget(btn_generate)
        layout.add_widget(btn_preview)
        layout.add_widget(btn_save)

        return layout

    def generate(self, instance):
        text = self.text.text.strip()
        if not text:
            self.popup("Error", "Enter some text")
            return

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        choice = self.voice.text.lower()

        for v in voices:
            name = v.name.lower()
            lang = str(v.languages).lower()
            if choice == "male" and "male" in name:
                engine.setProperty('voice', v.id)
            elif choice == "female" and "female" in name:
                engine.setProperty('voice', v.id)
            elif choice == "hindi" and ("hi" in lang or "hindi" in name):
                engine.setProperty('voice', v.id)

        engine.setProperty('rate', 150)

        filename = f"tts_{int(time.time())}.wav"
        self.audio_file = os.path.join(self.user_data_dir, filename)

        engine.save_to_file(text, self.audio_file)
        engine.runAndWait()

        self.popup("Success", "Audio generated successfully")

    def preview(self, instance):
        if not self.audio_file:
            self.popup("Error", "Generate audio first")
            return
        sound = SoundLoader.load(self.audio_file)
        if sound:
            sound.play()

    def save(self, instance):
        if not self.audio_file:
            self.popup("Error", "Generate audio first")
            return
        self.popup("Saved", f"Saved at:\n{self.audio_file}")

    def popup(self, title, msg):
        Popup(title=title, content=Label(text=msg),
              size_hint=(0.8, 0.4)).open()

if __name__ == "__main__":
    TextToAudio().run()
