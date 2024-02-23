'''
Character class that represents a character in the Lord of the Mysteries.
'''

from mystic import objectStructures


class Character(objectStructures.CharacterStructure):
    """
    A class that represents a character in the Lord of the Mysteries.
    Inherits from the CharacterStructure class in the objectStructures module.

    Attributes:
    name (str): The name of the character.
    chinese_name (list[tuple]): The Chinese names of the character as a list of tuple ~ (Chinese Name, English Translation).
    birth: The birth details of the character.
    gender: The gender of the character.
    species: The species of the character.
    height: The height of the character.
    eye_colour: The eye colour of the character.
    hair_colour: The hair colour of the character.
    aliases: The aliases of the character.
    titles: The titles of the character.
    pathways: The pathways of the character.
    authorities: The authorities of the character.
    relatives: The relatives of the character.
    masters: The masters of the character.
    enemies: The enemies of the character.
    allies: The allies of the character.
    image: The image of the character.
    affliation: The affliation of the character.
    occupation: The occupation of the character.
    religion: The religion of the character.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Character class.

        Parameters:
        name (str): The name of the character.
        """

        super().__init__(name)

        self.chinese_name = self.get_chinese_name()
        self.birth = self.get_birth()
        self.gender = self.get_gender()
        self.species = self.get_species()
        self.height = self.get_height()
        self.eye_colour = self.get_eye_colour()
        self.hair_colour = self.get_hair_colour()
        self.aliases = self.get_aliases()
        self.titles = self.get_titles()
        self.pathways = self.get_pathways()
        self.authorities = self.get_authorities()
        self.relatives = self.get_relatives()
        self.masters = self.get_masters()
        self.enemies = self.get_enemies()
        self.allies = self.get_allies()
        self.image = self.get_image()
        self.affliation = self.get_affliation()
        self.occupation = self.get_occupation()
        self.religion = self.get_religion()
        self.residence = self.get_residence()
        self.origin = self.get_origin()
        self.intro = self.get_intro()
        self.honorific_name = self.get_honorific_name()

    def get_name(self) -> str:
        """
        Returns the name of the character.

        Returns:
        str: The name of the character.
        """

        return self.parsed.find("h2", class_="pi-title").text

    def get_chinese_name(self) -> list[tuple]:
        """
        Returns the Chinese names of the character as a list of tuple ~ (Chinese Name, English Translation).

        Returns:
        list[tuple]: The Chinese names of the character.
        """

        names = []
        head = self.parsed.find("h3", string="Chinese")
        div = head.parent.find("div")

        children = div.findChildren("span")

        if len(children) == 0:
            names.append(div.text)

        for child in children:
            children2 = child.findChildren("i")
            if len(children2) != 0:
                continue
            names.append(child.text)

        return list(zip(names[0::2], names[1::2]))

    def get_birth(self) -> str:
        """
        Retrieves the birth information of the character.

        Returns:
            str: The birth information of the character, or None if not found.
        """

        head = self.parsed.find("h3", string="Birth")
        try:
            return head.parent.find("div").text
        except AttributeError:
            return None

    def get_gender(self) -> str:
        """
        Retrieves the gender of the character.

        Returns:
            str: The gender of the character, or None if not found.
        """

        head = self.parsed.find("h3", string="Gender")
        try:
            return head.parent.find("a").text
        except AttributeError:
            return None

    def get_species(self) -> list:
        """
        Retrieves the species of the character.

        Returns:
            list: A list of species of the character.
        """

        species = []
        head = self.parsed.find("h3", string="Species")
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[: data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    specie = child.text[: child.text.index("[")]
                except ValueError:
                    specie = child.text
                species.append(specie)
            return species
        except AttributeError:
            return None

    def get_height(self) -> list[str]:
        """
        Retrieves the height of the character.

        Returns:
            list[str]: A list of heights, where each height is a string.
        """

        heights = []
        head = self.parsed.find("h3", string="Height")
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[: data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    height = child.text[: child.text.index("[")]
                except ValueError:
                    height = child.text
                heights.append(height)
            return heights
        except AttributeError:
            return None

    def get_eye_colour(self) -> list:
        """
        Retrieves the eye color(s) of the character.

        Returns:
            list: A list of eye color(s) of the character.
                  If the eye color is not found, returns None.
        """

        eyes = []
        head = self.parsed.find("h3", string="Eye")
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[: data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    eye = child.text[: child.text.index("[")]
                except ValueError:
                    eye = child.text
                eyes.append(eye)
            return eyes
        except AttributeError:
            return None

    def get_hair_colour(self) -> list:
        """
        Retrieves the hair color(s) of the character.

        Returns:
            list: A list of hair color(s) of the character.
                  If no hair color is found, returns None.
        """

        hairs = []
        head = self.parsed.find("h3", string="Hair")
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[: data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    hair = child.text[: child.text.index("[")]
                except ValueError:
                    hair = child.text
                hairs.append(hair)
            return hairs
        except AttributeError:  # If the hair color is not found, return None
            return None

    def get_aliases(self) -> list[str]:
        """
        Retrieves the aliases of the character.

        Returns:
            A list of strings representing the aliases of the character.
            If no aliases are found, returns None.
        """

        aliases = []
        head = self.parsed.find("h3", string="Aliases")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            aliases.append(text)

        return aliases

    def get_titles(self) -> list[str]:
        """
        Retrieves the titles associated with the character.

        Returns:
            A list of strings representing the titles.
        """

        titles = []
        head = self.parsed.find("h3", string="Titles")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")
        if len(lists) == 0:
            return head.parent.find("div")

        for li in lists:
            s_text = ""
            for span in li.find_all("span"):
                try:
                    span["style"]
                except KeyError:
                    continue
                try:
                    s_text += span.text[: span.text.index("[")]
                except ValueError:
                    s_text += span.text
            try:
                text = f"{li.text[:li.text.index('[')]} ({s_text})"
            except ValueError:
                text = li.text + s_text
            titles.append(text)
        return titles

    def get_pathways(self) -> list[str]:
        """
        Retrieves the pathways associated with the character.

        Returns:
            list[str]: A list of pathway names.
        """

        pathways = []
        head = self.parsed.find("h3", string="Pathway(s)")

        try:
            head.parent
        except AttributeError:
            return None

        for a in head.parent.find_all("a"):
            if not a.text == "":
                try:
                    a["title"]
                except KeyError:
                    continue
                try:
                    l = a.text[: a.text.index("[")]
                    pathways.append(l)
                except:
                    pathways.append(a.text)
        return pathways

    def get_authorities(self) -> list[str]:
        """
        Retrieves the list of authorities associated with the character.

        Returns:
            list[str]: The list of authorities.
        """

        authorities = []
        head = self.parsed.find("h3", string="Authorities")

        try:
            head.parent
        except AttributeError:
            return None

        for a in head.parent.find_all("a"):
            if not a.text == "":
                try:
                    a["title"]
                except KeyError:
                    continue
                try:
                    text = a.text[: a.text.index("[")]
                except:
                    text = a.text
                authorities.append(text)
        if len(authorities) == 0:
            return None
        return authorities

    def get_relatives(self) -> list[str]:
        """
        Retrieves the list of relatives for the character.

        Returns:
            A list of strings representing the relatives of the character.
        """

        relatives = []
        head = self.parsed.find("h3", string="Relative(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            relatives.append(text)

        return relatives

    def get_masters(self) -> list[str]:
        """
        Retrieves the list of masters associated with the character.

        Returns:
            A list of strings representing the names of the masters.
            If no masters are found, returns None.
        """

        masters = []
        head = self.parsed.find("h3", string="Master(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            masters.append(text)

        return masters

    def get_enemies(self) -> list[str]:
        """
        Retrieves a list of enemies associated with the character.

        Returns:
            A list of strings representing the enemies.
        """

        enemies = []
        head = self.parsed.find("h3", string="Enemie(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            enemies.append(text)

        return enemies

    def get_allies(self) -> list[str]:
        """
        Retrieves a list of allies associated with the character.

        Returns:
            list[str]: A list of allies.
        """

        allies = []
        head = self.parsed.find("h3", string="Allies")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            allies.append(text)

        return allies

    def get_image(self) -> str:
        """
        Retrieves the image URL of the character.

        Returns:
            str: The URL of the character's image.
                If no image exists, returns "No Image exists yet."
        """

        try:
            figure_header = self.parsed.find("figure", class_="pi-item pi-image")
            return figure_header.find("img")["src"]
        except:
            return "No Image exists yet."

    def get_affliation(self) -> list[str]:
        """
        Retrieves the affiliations of the character.

        Returns:
            list[str]: A list of affiliations.
        """

        affliations = []
        head = self.parsed.find("h3", string="Affiliation(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            affliations.append(text)

        return affliations

    def get_occupation(self) -> list[str]:
        """
        Retrieves the occupation(s) of the character.

        Returns:
            A list of strings representing the occupation(s) of the character.
            If no occupation is found, returns None.
        """

        occupations = []
        head = self.parsed.find("h3", string="Occupation(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            occupations.append(text)

        return occupations

    def get_religion(self) -> list[str]:
        """
        Retrieves the religion(s) of the character.

        Returns:
            A list of strings representing the religion(s) of the character.
            If no religion is found, returns None.
        """

        religions = []
        head = self.parsed.find("h3", string="Religion(s)")

        try:
            head.parent
        except AttributeError:
            return None

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[: li.text.index("[")]
            except ValueError:
                text = li.text
            religions.append(text)

        return religions

    def get_origin(self) -> list[str]:

            """
            Retrieves the origin of the Character.

            Returns:

                A list of strings representing the origin of the character.
                If no origin is found, returns None.

            """



            origins = []
            head = self.parsed.find("h3" , string = 'Origin')

            try:
                head.parent
            except AttributeError:
                return [None]

            lists = head.parent.find_all("li")

            if len(lists) == 0:
                return head.parent.find("div").text

            for li in lists:
                try:
                    text = li.text[:li.text.index("[")]
                except ValueError:
                    text = li.text
                origins.append(text)

            return origins

    def get_residence(self) -> list[str]:

        """
            Retrieves the residence of the Character.

            Returns:

                A list of strings representing the Residences of the character.
                If no residence is found, returns None.

        """



        residences = []
        head = self.parsed.find("h3" , string = 'Residence')

        try:
            head.parent
        except AttributeError:
            return [None]

        lists = head.parent.find_all("li")

        if len(lists) == 0:
            return head.parent.find("div").text

        for li in lists:
            try:
                text = li.text[:li.text.index("[")]
            except ValueError:
                text = li.text
            residences.append(text)

        return residences

    def get_intro(self) -> list[str]:

        """
            Retrieves the intro of the Character.

            Returns:

                A list of strings representing the intro of the character.
                If no intro is found, returns None.

        """

        intros = self.parsed.find_all("p")[7:12]  
        intro_texts = [p.text.strip() for p in intros]  

        return intro_texts

    def get_honorific_name(self) -> list[str]:

        """
        Retrieves the honorific name of the character.

        Returns:
            A list of strings representing the honorific name of the character.

        """

        honorific = self.parsed.find_all("div" , class_ = "poem")
        if honorific[1:2] == []:  #fixes exceptions to the assumed position of honorific names in webpages
            honorific_text = [p.text.strip() for p in honorific[0:1]]


        else:
            honorific_text = [p.text.strip() for p in honorific[1:2]]       

        honorific_text = honorific_text[0].split('"') #splits the list at "
        honorific_text.remove('Simplified Chinese:\xa0上帝、创造者、造物主、全知全能者、星界之主') 
        # removes the popular pop up in honorific names

        return honorific_text



