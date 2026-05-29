from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class MasikPrativedanAutofiller(App):
    def build(self):
        # स्क्रॉल व्यू ताकि अगर फॉर्म बड़ा हो तो मोबाइल पर आसानी से ऊपर-नीचे हो सके
        root = ScrollView(size_hint=(1, 1), bar_width=10)
        
        # मुख्य लेआउट
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # ऐप की हेडिंग
        heading = Label(
            text="मासिक प्रतिवेदन Autofiller", 
            font_size='26sp', 
            bold=True, 
            size_hint_y=None, 
            height=50,
            color=(0.1, 0.6, 0.4, 1) # सुंदर हरा रंग
        )
        layout.add_widget(heading)
        
        # विवरण टेक्स्ट
        sub_text = Label(
            text="अपना विवरण नीचे भरें, ऐप इसे ऑटोमैटिक फिल कर देगा:",
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1)
        )
        layout.add_widget(sub_text)
        
        # इनपुट फील्ड्स (यहाँ यूजर अपना डेटा भरेगा)
        self.inputs = {}
        fields = ["कर्मचारी का नाम", "पदनाम", "विभाग / कार्यालय", "महीना और वर्ष", "कुल कार्य दिवस"]
        
        for field in fields:
            # फील्ड का नाम (Label)
            lbl = Label(text=field, font_size='18sp', size_hint_y=None, height=30, halign='left', text_size=(Window.width - 60, None))
            layout.add_widget(lbl)
            
            # लिखने की जगह (TextInput)
            txt_input = TextInput(
                hint_text=f"{field} यहाँ लिखें...", 
                multiline=False, 
                size_hint_y=None, 
                height=45,
                padding=[10, 10, 10, 10],
                background_normal='',
                background_color=(0.95, 0.95, 0.95, 1)
            )
            layout.add_widget(txt_input)
            self.inputs[field] = txt_input
            
        # ऑटोफिल करने वाला जादुई बटन
        btn_submit = Button(
            text="🚀 Autofill Form", 
            font_size='20sp', 
            bold=True,
            size_hint_y=None, 
            height=55,
            background_normal='',
            background_color=(0.1, 0.6, 0.4, 1),
            color=(1, 1, 1, 1)
        )
        btn_submit.bind(on_press=self.start_autofill)
        layout.add_widget(btn_submit)
        
        # स्टेटस दिखाने के लिए नीचे की जगह
        self.status_lbl = Label(text="", font_size='16sp', size_hint_y=None, height=40, color=(0.2, 0.2, 0.8, 1))
        layout.add_widget(self.status_lbl)
        
        root.add_widget(layout)
        return root

    def start_autofill(self, instance):
        # जब यूजर बटन दबाएगा तो यह फंक्शन चलेगा
        name = self.inputs["कर्मचारी का नाम"].text
        if not name:
            self.status_lbl.text = "⚠️ कृपया कम से कम नाम ज़रूर भरें!"
            self.status_lbl.color = (0.8, 0.2, 0.2, 1)
        else:
            self.status_lbl.text = f"✅ {name} का प्रतिवेदन सफलतापूर्वक ऑटोफिल हो रहा है..."
            self.status_lbl.color = (0.1, 0.6, 0.2, 1)

if __name__ == '__main__':
    MasikPrativedanAutofiller().run()

