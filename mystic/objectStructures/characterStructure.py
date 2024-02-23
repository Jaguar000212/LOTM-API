"""Structure for Characters class of the API."""

import requests
import bs4
import mystic.helpers as helpers

WEB_URL = "https://lordofthemysteries.fandom.com/wiki/"


class CharacterStructure:
    """Represents a character in the Lord of the Mysteries universe."""

    def __init__(self, name: str):
        """
        Initializes a CharacterStructure object.

        Parameters:
        - name (str): The name of the character.

        Raises:
        - NotFoundError: If the character is not found on the website.
        """
        self.url_name = helpers.misc.format_name(name)
        self.url = WEB_URL + self.url_name
        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            raise helpers.exceptions.NotFoundError("Character not found.")

        self.parsed = bs4.BeautifulSoup(self.response.text, "html.parser")
        self.name = self.get_name()

    def get_name(self):
        """
        Retrieves the name of the character.

        Returns:
        - str: The name of the character.
        """
        pass

    def get_data(self) -> dict:
        """
        Retrieves the data of the character.

        Returns:
        - dict: The data of the character.
        """
        data = self.__dict__
        data.pop("response")
        data.pop("parsed")
        data.pop("url_name")

        return data

    def __str__(self) -> str:
        """
        Returns a string representation of the character.

        Returns:
        - str: The string representation of the character.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Returns a string representation of the character.

        Returns:
        - str: The string representation of the character.
        """
        return self.name

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.

        Parameters:
        - key: The key to retrieve the value for.

        Returns:
        - The value associated with the given key.
        """
        return self.__dict__[key]

    def __iter__(self):
        """
        Iterates over the character's attributes.

        Yields:
        - Tuple[str, Any]: A tuple containing the attribute name and its value.
        """
        for key, value in self.__dict__.items():
            yield key, value
