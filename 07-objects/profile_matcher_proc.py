def build_profile(age, *hobbies):
    profile = {"age":age, "hobbies": hobbies}
    return profile

def match(profile_1, profile_2):
    match_quality = 0
    age_diff = abs(profile_1["age"] - profile_2["age"])#abs works with neg or pos numbers
    if age_diff <= 5:
        match_quality += 1
    for hobby in profile_1["hobbies"]:
        if hobby in profile_2["hobbies"]:#membership operator
            match_quality += 1
    return match_quality

profile_1 = build_profile(30, "cheese", "wine")
profile_2 = build_profile(32, "wine", "beer")
print(match(profile_1, profile_2))
