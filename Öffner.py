import webbrowser

def open_youtube():
    url = "https://www.youtube.com/"
    webbrowser.open(url)

# Beispielanwendung
if __name__ == "__main__":
    for _ in range(100):
        open_youtube()

