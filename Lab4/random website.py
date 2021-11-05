import random
import webbrowser

websites = ("www.facebook.com", "www.google.com", "www.youtube.com", "www.twitter.com", "www.w3schools.com")
index = int(random.uniform(0, 5))
webbrowser.open(f"https://{websites[index]}")
