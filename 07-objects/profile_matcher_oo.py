class ProfileBuilder:
    def __init__(self, age, *hobbies):
        self.age = age
        self.hobbies = hobbies

class Matcher:
    def __init__(self):
        self.match_quality = 0
        self.age_diff = 0
    def match(self, profile_1, profile_2):
        match_quality = 0
        age_diff = abs(profile_1.age - profile_2.age)    
        if age_diff <= 5:
            match_quality += 1
        for hobby in profile_1.hobbies:
            if hobby in profile_2.hobbies:#membership operator
                match_quality += 1
        return match_quality

# executable code in the module is protected from access in the calling script
if __name__ == '__main__': 
    profile_1 = ProfileBuilder(30, "cheese", "wine")
    profile_2 = ProfileBuilder(32, "wine", "beer", "perry")
    matcher = Matcher()
    print(matcher.match(profile_1, profile_2))
