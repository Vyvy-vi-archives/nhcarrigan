import colorama
from colorama import Fore, Back, Style

def bio():
    """Holds Nick's bio"""
    bio_text = "I am a web developer focusing on the MEAN stack with a love for TypeScript. Development is a passion of mine, which began with the FreeCodeCamp curriculum on 15 April 2020. Since then, I have continued to learn, grow, and acquire new skills. I am eager to further my knowledge and ability in a paid developer role.\nIn my free time I enjoy playing a video game or reading a book. I enjoy learning new skills and picking up random bits of trivia. For example, did you know that an 'emordnilap' is a word which when reversed spells another word?\nI am a firm believer in open-source. All of my project files are available on GitHub, and I am open to Pull Requests and suggestions on all of them. If you'd like to contribute, you can access my GitHub profile via the 'socials' function"
    return bio_text

def socials():
    """Returns Nick's socials"""
    social_links = {
            'Resume' : "https://www.nhcarrigan.com/assets/files/Resume.pdf",
            'FreeCodeCamp Forum' : "https://forum.freecodecamp.org/u/nhcarrigan",
            'Github' : "https://github.com/nhcarrigan",
            'Facebook' : "https://www.facebook.com/nhcarrigan",
            'LinkedIn' : "https://www.linkedin.com/in/nhcarrigan",
            'Twitter' : "https://www.twitter.com/nhcarrigan",
            'Steam' : "https://steamcommunity.com/id/nhcarrigan",
            'Skype' : "https://join.skype.com/invite/uiGryTXNEt26",
            'Discord' : "chat.nhcarrigan.com" }
    return social_links


def certifications():
    """Returns nicks certificates"""
    certs = {
        'FreeCodeCamp': [
            ('Quality Assurance V7 - Earned 3 July 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/quality-assurance-v7'),
             ('Scientific Computing with Python - Earned 3 July 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/scientific-computing-with-python-v7'),
             ('Full Stack Developer - Earned 25 May 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/full-stack'),
             ('Responsive Web Design - Earned 18 April 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/responsive-web-design'),
             ('Javascript Algorithms and Data Structures - Earned 24 April 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/javascript-algorithms-and-data-structures'),
             ('Front End Libraries - Earned 29 April 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/front-end-libraries'),
             ('Data Visualisation - Earned 25 May 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/data-visualization'),
             ('APIs and Microservices - Earned 8 May 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/apis-and-microservices'),
             ('Information Security and Quality Assurance - Earned 19 May 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/information-security-and-quality-assurance'),
             ('Legacy Front End - Earned 14 August 2020', 'https://www.freecodecamp.org/certification/nhcarrigan/legacy-front-end')],
        'Google Digital Garage': [
             ('Fundamentals of Digital Marketing - Earned 7 May 2020', 'https://www.nhcarrigan.com/assets/files/Digital%20Marketing.pdf')]
             }
    return certs

class color:
   PURPLE = '\033[95m'
   PURP = '\033[48;2;84;22;52m'
   BECCA = '\033[48;2;97;2;127m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



if __name__ == '__main__':
    colorama.init()
    bio = bio()
    socials = socials()
    cert = certifications()
    print(Back.MAGENTA + Style.BRIGHT)
    print(color.BOLD + color.CYAN + color.UNDERLINE+ 'Nicholas Carrigan' + color.END)
    print(color.PURP + Style.BRIGHT)
    print(f'\n{Fore.GREEN}About me:{Fore.RESET}\n{bio}')
    print(f'\n{Fore.GREEN}Connect with me:{Fore.RESET}')
    for site  in socials:
        print(f'{site} :  {socials[site]}')
    print(f'\n{Fore.GREEN}My Certifications:{Fore.RESET}\n')
    for platform in cert:
        print('\t' + color.BOLD + Fore.LIGHTYELLOW_EX + platform + Fore.RESET + color.END + color.PURP + Style.BRIGHT)
        print(*[f'{course[0]}: {course[1]}' for course in cert[platform]], sep ='\n')
        print('\n')
