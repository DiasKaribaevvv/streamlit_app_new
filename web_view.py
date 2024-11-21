from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix. import WebView

class WebViewApp(App):
    def build(self):
        layout = BoxLayout()
        webview = WebView(url="http://localhost:8501")  # URL Streamlit-приложения
        layout.add_widget(webview)
        return layout

if __name__ == '__main__':
    WebViewApp().run()
