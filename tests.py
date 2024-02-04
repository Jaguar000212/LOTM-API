import unittest
from mystic import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character1 = Character("Klein Moretti")  # Initialize your class here
        self.character2 = Character("Fors Wall")

    def test1(self):
        # Call the method you want to test
        result = self.character1.get_data()
        expected_result = {
            'url': 'https://lordofthemysteries.fandom.com/wiki/Klein_Moretti', 
            'name': 'Klein Moretti', 
            'chinese_name': [('克莱恩·莫雷蒂', 'Klein Moretti'), ('周明瑞', 'Zhou Mingrui')], 
            'birth': 'March 4th, 1327', 
            'gender': 'Male', 
            'species': ['Mythical Creature ', 'Human (Former)'], 
            'height': ['1.72 meters (Debut)', '1.80 meters (Chapter 1268)'], 
            'eye_colour': ['Black', 'Brown (Former)'],
            'hair_colour': 'Black', 
            'aliases': ['The Fool\xa0(愚者)', 'The World\xa0(世界)', 'Sherlock Moriarty\xa0(夏洛克·莫里亚蒂)', 'Hero Bandit Black Emperor', 'Gehrman Sparrow\xa0(格尔曼·斯帕罗)', 'Sea God Kalvetua', 'Sinbad Voluntier (Temporary)', 'John Yode (Temporary)', 'Dwayne Dantès\xa0(道恩·唐泰斯)', 'Clown Angel', 'Mr. Clown', 'Merlin Hermes\xa0(梅林·赫尔墨斯})', 'Miracle Magician', 'Mysteries\xa0(诡秘) (By Ancient Sun God, True Creator and Adam)', 'Blasphemer (By Steph)'], 
            'titles': ['Sea God ()', 'Craziest Hunter ()', 'Strongest Adventurer of the Five Seas ()', 'Angel of Redemption (As Gehrman Sparrow) ((As Gehrman Sparrow))', 'The Fool  ()', 'Half-Lord of MysteriesKing of Space-Time,Beacon of Destiny,Embodiment of Sefirah Castle,Dominator of the Spirit World,Lord of Mysteries (Lord of MysteriesKing of Space-Time,Beacon of Destiny,Embodiment of Sefirah Castle,Dominator of the Spirit World,Lord of Mysteries)'], 
            'pathways': ['Fool'], 
            'authorities': ['Fool', 'Door', 'Error'], 
            'relatives': ['Unnamed Father†', 'Unnamed Mother†', 'Benson Moretti (Elder Brother)', 'Melissa Moretti (Younger Sister)', "Unnamed Niece (Benson's Daughter)"], 
            'masters': ['Azik Eggers', 'Roselle Gustav (Through Diary)', 'Old Neil†'], 
            'enemies': ['Outer Deities', 'The Celestial Worthy of Heaven and Earth', 'Adam', 'Amon', 'Zaratul', 'Ince Zangwill†', 'Lanevus†'], 
            'allies': ['Evernight Goddess', 'Reinette Tinekerr (Messenger)', 'Will Auceptin', 'Azik Eggers', 'Bernadette Gustav', 'Pallez Zoroast'], 
            'image': 'https://static.wikia.nocookie.net/lord-of-the-mystery/images/4/4c/Klein_Moretti_Official.jpg/revision/latest/scale-to-width-down/246?cb=20201017102316', 
            'affliation': ['Tarot Club', 'Church of the FoolChurch of the Sea GodCity of SilverMoon CityTemperance Faction of Rose School of Thought', 'Church of the Sea God', 'City of Silver', 'Moon City', 'Temperance Faction of Rose School of Thought', 'Life School of Thought', 'Church of the Evernight GoddessNighthawks (Former)Blackthorn Security Company (Former)', 'Nighthawks (Former)', 'Blackthorn Security Company (Former)', 'Adventurer Association'], 'occupation': ['Transmigrator', 'Founder of the Tarot Club', 'God of Church of the Fool', 'The current owner of the Sefirah Castle', 'History Graduate', 'Nighthawk', 'Fortune-Teller at the Divination Club', 'Inspector of Tingen Police Department', 'Detective', 'Bodyguard (Temporary)', 'Shareholder of Backlund Bike Company (Former)', 'Adventurer', 'Bounty Hunter', 'Volunteer (Temporary)', 'Angel of Redemption under The Fool', 'Merchant', 'Founder and symbolic role director of the Loen Charity Bursary Foundation', 'Leader of Numinous Episcopate faction in Backlund', 'Shareholder of Coim Company (Former)', 'Arms Dealer', 'Wandering Magician'], 'religion': ['Church of the Fool (As Gehrman Sparrow and Merlin Hermes)', 'Church of the Evernight Goddess (Nominally, as Klein Moretti and Dwayne Dantès)', 'Church of the God of Steam and Machinery (As Sherlock Moriarty)']}
        # Assert that the result is as expected
        self.assertEqual(result, expected_result)

    def test2(self):
        result = self.character2.get_data()
        expected_result = {'url': 'https://lordofthemysteries.fandom.com/wiki/Fors_Wall', 
                           'name': 'Fors Wall', 
                           'chinese_name': [], 
                           'birth': '13 April 1326', 
                           'gender': 'Female', 
                           'species': 'Human', 
                           'height': '1.65 meters', 
                           'eye_colour': 'Light Blue', 
                           'hair_colour': 'Brown', 
                           'aliases': ['The Magician', 'Margaret Taylor', 'Slacker Without a Dream'], 
                           'titles': 'Angel of Stars', 
                           'pathways': ['Door'], 
                           'authorities': None, 
                           'relatives': ['Unnamed Father (Remarried)', 'Unnamed Mother †'], 
                           'masters': ['Dorian Gray Abraham', 'Mr. Door (Unconventional)'], 
                           'enemies': ['Traitors of Abraham FamilyBotis†Mr.X†', 'Botis†', 'Mr.X†'], 
                           'allies': None, 
                           'image': 'https://static.wikia.nocookie.net/lord-of-the-mystery/images/0/0e/Fors_Wall_Official.jpg/revision/latest/scale-to-width-down/223?cb=20210306083856', 
                           'affliation': ['Tarot Club (Major Arcana)', 'Abraham Family', 'Church of the Fool'], 
                           'occupation': ['Author', 'Angel of Church of the Fool', 'Clinical Doctor (Former)'], 
                           'religion': ['Church of the Fool', 'Church of the God of Steam and Machinery (Former)']}
        self.assertEqual(result, expected_result)

# More tests...

if __name__ == '__main__':
    unittest.main()