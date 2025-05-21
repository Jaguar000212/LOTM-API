# Mystic ✨

An API to access all the major details of any character from the well-renowned novel, `The Lord of the Mysteries`.  
The API extracts data from the website "https://lordofthemysteries.fandom.com/wiki/"
> The API is under development. Some elements may contain bugs, and more features are upcoming.

---

### - ⚒️ Requirements
- `requests` for retrieving the webpage.
- `BeautifulSoup` for HTML parsing and scraping.
- `NLTK` for the correct generation of the URL.

---

### - 💻 Installation
Simply clone the repo and use the `Character` class.

```sh
# Install the requirements
$ python3 pip install requests bs4 nltk

# Clone the repository
$ git clone https://github.com/Jaguar000212/LOTM-API.git

# Change the directory
$ cd LOTM-API
```

 ---

 ### - 📃 Usage

```py
import mystic


character = api.Character(name = "Klein Moretti")
print(character.get_data())
```


---

### - 🟢 What more?
We will be updating the API with more classes, bug fixes, efficiency, and readability. We are working on the documentation as well. <br>
Contributions are welcome!  
> Currently, the development has been halted; contributions are welcome.

---

With ❤️ by [Jaguar000212](https://github.com/Jaguar000212/) & [Theroid00](https://github.com/Theroid00/)
