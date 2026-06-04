import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

# We will use the Google GenAI SDK for the Gemini API connection
import google.generativeai as genai

# Configure the API key. 
# For security, the app will look for an environment variable, 
# or you can temporarily paste your key here later.
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
genai.configure(api_key=API_KEY)

class PrigAiLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PrigAiLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Header Title
        self.title_label = Label(
            text="Prig AI Assistant", 
            font_size='24sp', 
            size_hint_y=0.1,
            bold=True
        )
        self.add_widget(self.title_label)

        # Scrollable area for responses
        self.scroll_view = ScrollView(size_hint_y=0.6)
        self.response_label = Label(
            text="Welcome to Prig AI! Ask me anything below.", 
            font_size='16sp', 
            size_hint_y=None,
            text_size=(400, None), # Will dynamically update later
            halign='left',
            valign='top'
        )
        self.response_label.bind(texture_size=self.response_label.setter('size'))
        self.scroll_view.add_widget(self.response_label)
        self.add_widget(self.scroll_view)

        # User Input Box
        self.user_input = TextInput(
            hint_text="What's on your mind today?", 
            multiline=True, 
            size_hint_y=0.2,
            font_size='16sp'
        )
        self.add_widget(self.user_input)

        # Submit Button
        self.submit_btn = Button(
            text="Send to Prig AI", 
            size_hint_y=0.1, 
            background_color=(0.1, 0.6, 0.8, 1),
            font_size='18sp',
            bold=True
        )
        self.submit_btn.bind(on_press=self.on_submit)
        self.add_widget(self.submit_btn)

    def on_submit(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return

        # Clear input and update status safely
        self.user_input.text = ""
        self.response_label.text = "Prig AI is thinking..."
        self.submit_btn.disabled = True

        # Run the API call in a background thread so the app UI never freezes or loops continuously
        threading.Thread(target=self.fetch_ai_response, args=(query,)).start()

    def fetch_ai_response(self, query):
        try:
            # Adjust response width to match the screen size dynamically
            self.response_label.text_size = (self.scroll_view.width - 20, None)
            
            # Calling the official Gemini model
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(query)
            
            # Send the result back to the main UI thread safely
            Clock.schedule_once(lambda dt: self.update_ui(response.text), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_ui(f"Error: {str(e)}\n\nMake sure your API key is correct and connected to the internet."), 0)

    def update_ui(self, text):
        self.response_label.text = text
        self.submit_btn.disabled = False

class PrigAiApp(App):
    def build(self):
        return PrigAiLayout()

if __name__ == '__main__':
    PrigAiApp().run()
