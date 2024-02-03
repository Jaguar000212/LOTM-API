# The Lord of the Mystries

An API to access all the major details of any charcter from the well renouned novel!
The API extracts data from the website "https://lordofthemysteries.fandom.com/wiki/"
> The API is under developement. Some elements may contain bugs, more features upcoming.

---

### - Requirements
- `requests` for retrieving the webpage.
- `BeautifulSoup` for HTML parsing and scraping.
- `NLTK` for correct generation of the url.

---

### - Installation
Simply clone the the repo, and use the `Character` class.

 ---

 ### - Usage

```py
import api


character = api.Character(name = "Klein Moretti")
print(character.get_data())
```


---

### - What more?
We will be updating the API with more objects, with bug fixes, efficiency and readability.
Contributions are welcome!

---

With ❤️ by [Jaguar000212](https://github.com/Jaguar000212/) & [Theroid00](https://github.com/Theroid00/)