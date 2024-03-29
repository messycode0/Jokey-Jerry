# MIT License

# Copyright (c) 2022 Jacob O'Bbrien

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class everyone:
    list_of_people = [
        "everyone",
        "immaculata",
        "jake",
        "beecie",
        "bon",
        "ella",
    ]

    def __init__(self):
        self.jokes = [
            "NULL"
        ]

    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)

class immaculata:
    def __init__(self):
        self.jokes = [
            "Why did the chicken cross the road? To get Micky D\’s",
            "What do you call a fake noodle? An impasta",
            "\“Your mother has been with us for 20 years,\” said John. \“Isn\’t it time she got a place of her own?\”\n\“My mother?\” replied Helen. \“I thought she was your mother.\”",
            "Police arrested two kids yesterday, one was drinking battery acid, the other was eating fireworks. They charged one – and let the other one off.",
            "My therapist says I have a preoccupation with vengeance. We\’ll see about that.",
            "A guy is sitting at home when he hears a knock at the door. He opens the door and sees a snail on the porch. He picks up the snail and throws it as far as he can. Three years later there\’s a knock on the door. He opens it and sees the same snail. The snail says: \‘What the hell was that all about?\’"
        ]

    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)

class jake:
    def __init__(self):
        self.jokes = [
            "joke is right here, or is it?",
            "then he said \" listen here you little shi-\" so i was like ca-pow",
            "chickens am I right lol, loves playing **chicken**",
            "cows am I right lol, being a **cow**ward",
            "sheep am I right lol, being all **sheepy** and stuff",
            "Fish am I right? Lol, being all **fishy** and stuff",
            "\"NOW GET A LIFE\" he said at the cematary",
        ]

    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)

class beecie:
    def __init__(self):
        self.jokes = [
            "A man walks into a library and asks the librarian for books about paranoia. She whispers, \"They're right behind you!\"",
            "Want to hear a roof joke? The first one's on the house.",
            "What should you do if you're attacked by a group of clowns? Go straight for the juggler.\nWhy don't koalas count as bears? They don't have the right koalafications.",
            "A cement mixer and a prison bus crashed on the highway. Police advise citizens to look out for a group of hardened criminals.",
            "I couldn't figure out why the baseball kept getting bigger. Then it hit me.",
            "I saw a movie about how ships are put together. It was riveting.",
            "What happens to a frog's car when it breaks down? It gets toad away.",
            "frogs am I right? Lol",
        ]
    
    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)

class bon:
    def __init__(self):
        self.jokes = [
            "A chef cooked his beef on the Eiffel Tower, the steaks had never been higher.",
            "Ladies first? That’s not what Genesis would tell you.",
            "What happens if you water a Led Zeppelin seed? You grow a Robert Plant.",
            "I don’t like telling jokes, because people laugh in my face.",
            "A kid walks up to his dad and asks. \“Daddy what\’s another word for killing yourself?\” And the dad says, \“Well I guess that would be suicide sonny.\” And the kid says \“But you said suicide is never the answer.\”",
            "I made a joke up on the fly, but sadly I was too big for it, and it had a crash landing.",
            "I’ll tell another joke when pigs fly, or better yet yo mama.",
            "Have you ever had that one friend who laughs louder then a Blue Whale’s mating call? And you know you don’t want to make them feel bad, I mean the whole world should be filled with laughter, just usually not all by the same person.",
            "What did the egg say to the cook? You crack me up.",
            "Why couldn’t you live without legs? Because you couldn’t stand it.",
            "I’ve heard people say they wanna get a light Buzz. But from what I’m seeing, they want more then a light buzz. They wanna be like Buzz Lightyear they wanna go to infinity and beyond.",
            "What happened to the nervous duck? He quaked under pressure.",
        ]
    
    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)

class ella:
    def __init__(self):
        self.jokes = [
            "What did the custodian say when he jumped out of the closet? \"Supplies!\"",
            "What does a baby computer call its father?\n\n\nData.",
            "Why don't oysters donate to charity? Because they're shellfish",
            "what do sprinters eat before a race? nothing. They fast"
        ]

    def get_joke(self):
        return self.jokes
    
    def get_random_joke(self):
        import random
        return random.choice(self.jokes)










if __name__ == "__main__":
    print("This is a module, not a script. Please run src/main.py\n\n")
    print("This module contains the following classes:")
    everyone = everyone()
    for i in everyone.list_of_people:
        print(i)
    print("\n")
    print("This module contains the following functions:")
    print("[NAME].get_joke()")
    print("[NAME].get_random_joke()")
    print("\n")
    print("heres a random joke from immaculata:")
    immaculata = immaculata()
    print(immaculata.get_random_joke())
    print("\n")
    print("heres a random joke from jake:")
    jake = jake()
    print(jake.get_random_joke())
    print("\n")

    del jake
    del immaculata
    del everyone

    print("have a good day!\n\nMADE BY JAKE (MESSYCODE) AND IMMACULATA (IMMACULATA RODIGO)\nTHIS SOFTWARE IS LICENSED UNDER THE MIT LICENSE\nMADE ON DEC 28 2022, AT (ALL DAY)\nVERSION:9999\n")
    exit()



