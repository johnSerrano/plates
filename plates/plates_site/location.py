def generic_check(license):
    license = [i for i in license if i.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890']
    if len(license) > 8:
        raise Exception("Bad license")

class location:
    location = None
    @staticmethod
    def check_license(license):
        raise NotImplementedError("Abstract class")

class Alabama(location):
    location="Alabama"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Alaska(location):
    location="Alaska"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Arizona(location):
    location="Arizona"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Arkansas(location):
    location="Arkansas"
    @staticmethod
    def check_license(license):
        generic_check(license)

class California(location):
    location="California"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Colorado(location):
    location="Colorado"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Connecticut(location):
    location="Connecticut"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Delaware(location):
    location="Delaware"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Florida(location):
    location="Florida"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Georgia(location):
    location="Georgia"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Hawaii(location):
    location="Hawaii"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Idaho(location):
    location="Idaho"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Illinois(location):
    location="Illinois"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Indiana(location):
    location="Indiana"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Iowa(location):
    location="Iowa"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Kansas(location):
    location="Kansas"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Kentucky(location):
    location="Kentucky"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Louisiana(location):
    location="Louisiana"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Maine(location):
    location="Maine"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Maryland(location):
    location="Maryland"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Massachusetts(location):
    location="Massachusetts"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Michigan(location):
    location="Michigan"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Minnesota(location):
    location="Minnesota"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Mississippi(location):
    location="Mississippi"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Missouri(location):
    location="Missouri"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Montana(location):
    location="Montana"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Nebraska(location):
    location="Nebraska"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Nevada(location):
    location="Nevada"
    @staticmethod
    def check_license(license):
        generic_check(license)

class New_Hampshire(location):
    location="New Hampshire"
    @staticmethod
    def check_license(license):
        generic_check(license)

class New_Jersey(location):
    location="New Jersey"
    @staticmethod
    def check_license(license):
        generic_check(license)

class New_Mexico(location):
    location="New Mexico"
    @staticmethod
    def check_license(license):
        generic_check(license)

class New_York(location):
    location="New York"
    @staticmethod
    def check_license(license):
        generic_check(license)

class North_Carolina(location):
    location="North Carolina"
    @staticmethod
    def check_license(license):
        generic_check(license)

class North_Dakota(location):
    location="North Dakota"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Ohio(location):
    location="Ohio"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Oklahoma(location):
    location="Oklahoma"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Oregon(location):
    location="Oregon"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Pennsylvania(location):
    location="Pennsylvania"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Rhode_Island(location):
    location="Rhode Island"
    @staticmethod
    def check_license(license):
        generic_check(license)

class South_Carolina(location):
    location="South Carolina"
    @staticmethod
    def check_license(license):
        generic_check(license)

class South_Dakota(location):
    location="South Dakota"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Tennessee(location):
    location="Tennessee"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Texas(location):
    location="Texas"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Utah(location):
    location="Utah"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Vermont(location):
    location="Vermont"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Virginia(location):
    location="Virginia"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Washington(location):
    location="Washington"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Washington_DC(location):
    location="Washington, DC"
    @staticmethod
    def check_license(license):
        generic_check(license)

class West_Virginia(location):
    location="West Virginia"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Wisconsin(location):
    location="Wisconsin"
    @staticmethod
    def check_license(license):
        generic_check(license)

class Wyoming(location):
    location="Wyoming"
    @staticmethod
    def check_license(license):
        generic_check(license)

locations=[
    Alabama,
    Alaska,
    Arizona,
    Arkansas,
    California,
    Colorado,
    Connecticut,
    Delaware,
    Florida,
    Georgia,
    Hawaii,
    Idaho,
    Illinois,
    Indiana,
    Iowa,
    Kansas,
    Kentucky,
    Louisiana,
    Maine,
    Maryland,
    Massachusetts,
    Michigan,
    Minnesota,
    Mississippi,
    Missouri,
    Montana,
    Nebraska,
    Nevada,
    New_Hampshire,
    New_Jersey,
    New_Mexico,
    New_York,
    North_Carolina,
    North_Dakota,
    Ohio,
    Oklahoma,
    Oregon,
    Pennsylvania,
    Rhode_Island,
    South_Carolina,
    South_Dakota,
    Tennessee,
    Texas,
    Utah,
    Vermont,
    Virginia,
    Washington,
    Washington_DC,
    West_Virginia,
    Wisconsin,
    Wyoming,
]
