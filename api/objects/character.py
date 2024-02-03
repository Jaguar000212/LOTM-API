'''
Character Object
'''

from api import objectStructures


class Character(objectStructures.CharacterStructure):
    
    '''A class that represents a character in the Lord of the Mystries'''
    
    def __init__(self , name : str) -> None:
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
        
    def get_name(self) -> str:
        
        '''Returns the name of the character.'''
        
        return self.parsed.find("h2" , class_ = "pi-title").text
    

    def get_chinese_name(self) -> list[tuple]:
        
        '''Returns the Chinese names of the character as a list of tuple ~ (Chinese Name, English Translation).'''
        
        names = []
        head = self.parsed.find("h3" , string = 'Chinese')
        div = head.parent.find("div")
        
        children = div.findChildren("span")
            
        if len(children) == 0:
            names.append(div.text)
        
        for child in children:
            children2 = child.findChildren("i")
            if len(children2) != 0:
                continue
            names.append(child.text)
            
        return list(zip(names[0::2] , names[1::2]))
    
    def get_birth(self) -> str:
        
        '''Returns the birth of the character.'''
        
        head = self.parsed.find("h3" , string = 'Birth')
        try:
            return head.parent.find("div").text
        except AttributeError:
            return None
    
    def get_gender(self) -> str:
        
        '''Returns the Gender of the character.'''

        head = self.parsed.find("h3" , string = 'Gender')
        try:
            return head.parent.find("a").text
        except AttributeError:
            return None

    def get_species(self) -> list:
        
        '''Returns the species of the character.'''
            
        species = []
        head = self.parsed.find("h3" , string = 'Species')
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[:data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    specie = child.text[:child.text.index("[")]
                except ValueError:
                    specie = child.text
                species.append(specie)
            return species
        except AttributeError:
            return [None]
        
    def get_height(self) -> list[str]:
        
        '''Returns the height of the character.'''
        
        heights = []
        head = self.parsed.find("h3" , string = 'Height')
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[:data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    height = child.text[:child.text.index("[")]
                except ValueError:
                    height = child.text
                heights.append(height)
            return heights
        except AttributeError:
            return [None]
        
    def get_eye_colour(self) -> list:
        
        '''Returns the eye color of the character.'''
        
        eyes = []
        head = self.parsed.find("h3" , string = 'Eye')
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[:data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    eye = child.text[:child.text.index("[")]
                except ValueError:
                    eye = child.text
                eyes.append(eye)
            return eyes
        except AttributeError:
            return [None]
    
    def get_hair_colour(self) -> list:
        
        '''Returns the hair color of the character.'''
            
        hairs = []
        head = self.parsed.find("h3" , string = 'Hair')
        try:
            data = head.parent.find("div")
            children = data.findAll("li")
            if len(children) == 0:
                try:
                    return data.text[:data.text.index("[")]
                except ValueError:
                    return data.text
            for child in data.findAll("li"):
                try:
                    hair = child.text[:child.text.index("[")]
                except ValueError:
                    hair = child.text
                hairs.append(hair)
            return hairs
        except AttributeError:
            return [None]

    def get_aliases(self) -> list[str]:
        
        '''Returns the aliases of the character.'''

        aliases = []
        head = self.parsed.find("h3" , string = 'Aliases')
        
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
            aliases.append(text)
            
        return aliases

    def get_titles(self) -> list[str]:
        
        '''Returns the titles of the character.'''
          
        titles = []
        head = self.parsed.find("h3" , string = 'Titles')
        
        try:
            head.parent
        except AttributeError:
            return [None]
        
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
                    s_text += span.text[:span.text.index("[")]
                except ValueError:
                    s_text += span.text
            try:
                text = f"{li.text[:li.text.index('[')]} ({s_text})"
            except ValueError:
                text = li.text + s_text
            titles.append(text)
        return titles

    def get_pathways(self) -> list[str]:
        
        '''Returns the pathways of the character.'''

        pathways = []
        head = self.parsed.find("h3" , string = 'Pathway(s)')
        
        try:
            head.parent
        except AttributeError:
            return [None]
        
        for a in head.parent.find_all("a"):
            if not a.text == '':
                try:
                    a['title']
                except KeyError:
                    continue
                try:
                    l = a.text[:a.text.index("[")]
                    pathways.append(l)
                except:
                    pathways.append(a.text)
        return pathways

    def get_authorities(self) -> list[str]:
        
        '''Returns the authorities of the character.'''

        authorities = []
        head = self.parsed.find("h3" , string = 'Authorities')
        
        try:
            head.parent
        except AttributeError:
            return [None]
        
        for a in head.parent.find_all("a"):
            if not a.text == '':
                try:
                    a['title']
                except KeyError:
                    continue
                try:
                    text = a.text[:a.text.index("[")]
                except:
                    text = (a.text)
                authorities.append(text)
        if len(authorities) == 0:
            return [None]
        return authorities
        
    def get_relatives(self) -> list[str]:
        
        '''Returns the relatives of the character.'''
            
        relatives = []
        head = self.parsed.find("h3" , string = 'Relative(s)')
            
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
            relatives.append(text)
          
        return relatives
    
    def get_masters(self) -> list[str]:
        
        '''Returns the masters of the character.'''
            
        masters = []
        head = self.parsed.find("h3" , string = 'Master(s)')
            
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
            masters.append(text)
            
        return masters
    
    def get_enemies(self) -> list[str]:
        
        '''Returns the enemies of the character.'''
            
        enemies = []
        head = self.parsed.find("h3" , string = 'Enemie(s)')
            
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
            enemies.append(text)
        
        return enemies
    
    def get_allies(self) -> list[str]:
        
        '''Returns the allies of the character.'''
                
        allies = []
        head = self.parsed.find("h3" , string = 'Allies')
                
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
            allies.append(text)
        
        return allies
    
    def get_image(self) -> str:
        
        '''Returns the image of the character.'''
        
        try:
            figure_header = self.parsed.find("figure" , class_ = "pi-item pi-image")
            return figure_header.find("img")["src"]
        except:
            return "No Image exists yet." 
    
    def get_affliation(self) -> list[str]:
        
        '''Returns the affliation of the character.'''
        
        affliations = []
        head = self.parsed.find("h3" , string = 'Affiliation(s)')
        
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
            affliations.append(text)
        
        return affliations
        
    def get_occupation(self) -> list[str]:
            
            '''Returns the occupation of the character.'''
            
            occupations = []
            head = self.parsed.find("h3" , string = 'Occupation(s)')
            
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
                occupations.append(text)
            
            return occupations
    
    def get_religion(self) -> list[str]:
        
        '''Returns the religion of the character.'''
        
        religions = []
        head = self.parsed.find("h3" , string = 'Religion(s)')
        
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
            religions.append(text)
        
        return religions
