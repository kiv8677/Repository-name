from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import platform
import sqlite3, os, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import arabic_reshaper
from bidi.algorithm import get_display

# --- محرك إصلاح العربي (يعالج مشكلة المربعات) ---
def fix_ar(text):
    if not text: return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

class KhaznaApp(App):
    def build(self):
        # لون الخلفية (أسود فخم)
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        
        # إعداد قاعدة البيانات في مسار أندرويد الآمن
        self.db_path = os.path.join(self.user_data_dir, "v.db")
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS a (id INTEGER PRIMARY KEY, s TEXT, u TEXT, p TEXT)")
        
        return self.main_menu()

    def main_menu(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # العنوان باستخدام اسم الخط الجديد myfont.ttf
        layout.add_widget(Label(
            text=fix_ar("خزنة د. عبدالمنعم"),
            font_name="myfont.ttf", 
            font_size='32sp',
            color=(0, 0.68, 0.71, 1),
            size_hint_y=0.2
        ))

        # أزرار الوظائف (كما كانت في بايثون 3)
        actions = [
            ("إضافة حساب جديد", (0, 0.6, 0.6, 1)),
            ("تصدير النسخة الاحتياطية", (0.1, 0.5, 0.1, 1)),
            ("استيراد البيانات", (0.7, 0.4, 0, 1)),
            ("إحصائيات الخزنة", (0.4, 0.4, 0.4, 1))
        ]

        for text, color in actions:
            btn = Button(
                text=fix_ar(text),
                font_name="myfont.ttf",
                background_color=color,
                size_hint_y=0.15,
                background_normal='' # لجعل الزر أسرع في الاستجابة
            )
            layout.add_widget(btn)

        return layout

if __name__ == "__main__":
    KhaznaApp().run()
