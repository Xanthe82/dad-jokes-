import tkinter as tk
import requests
from random import choice
from pyfiglet import figlet_format


window = tk.Tk()
window.title("Dad jokes")
bgcol = "#78DEC7"
window.configure(bg=bgcol)


header = figlet_format("DAD JOKE!")
intro_label = tk.Label(window, text = header, bg = bgcol)
intro_label.pack()

instruction = tk.Label(window, text = "Let me tell you a joke! Give me a topic: ", bg = bgcol)
instruction.pack()

topic_entry = tk.Entry(window)
topic_entry.pack()


def joke_search(topic):
    url = f"https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers = {"Accept": "application/json"},
        params = {"term": topic}
    ).json()
    res = response["results"]
    #return res
    total_jokes = response["total_jokes"]
    return res, total_jokes

def run():
    topic = topic_entry.get()
    results = joke_search(topic)

    jokescreen = tk.Text(window, bg="#B1BCE6")
    jokescreen.pack()

    if total_jokes >1:
        jokescreen.insert(tk.END, f"\n I have {total_jokes} jokes about {topic}. Here's one:\n ")
        jokescreen.insert(tk.END, choice(results)['joke'])
    elif total_jokes == 1:
        jokescreen.insert(tk.END, f"\n I have one joke about {topic}. Here it is:\n ")
        jokescreen.insert(tk.END, results[0]['joke'])
    else:
        jokescreen.insert(tk.END, f"\n Sorry, I don't have any jokes about {topic}! Please try again.")


search_button = tk.Button(window, text = 'Find a joke', highlightbackground = "#D62AD0", command=run, padx=5, pady=5)
search_button.pack()

window.mainloop()