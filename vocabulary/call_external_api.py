import requests
import os

OXFORD_API_ID = os.environ.get("OXFORD_API_ID")
OXFORD_API_KEY = os.environ.get("OXFORD_API_KEY")


class CallExternalOxford:
    def __init__(self, word):
        self.word = word
        self.root = ""
        self.status_code = {}
        self.app_id = OXFORD_API_ID
        self.app_key = OXFORD_API_KEY

    def call_api(self, endpoint):
        # set url filter
        # url = https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/pretty?fields=definitions%2Cpronunciations&strictMatch=false
        if endpoint == "entries":
            url = (
                f"https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/"
                + self.word.lower()
            )
        elif endpoint == "lemmas":
            url = (
                f"https://od-api.oxforddictionaries.com:443/api/v2/lemmas/en/"
                + self.word.lower()
            )
        else:
            return f"Endpoint {endpoint} not found. Please try again."

        # call API
        r = requests.get(url, headers={"app_id": self.app_id, "app_key": self.app_key})
        self.status_code[endpoint] = r.status_code
        if r.status_code == 200:
            return r.json()

    def call_lemmas(self):
        """retrieve and save the root of the word"""
        result = self.call_api("lemmas")
        if isinstance(result, str):
            print(result)
        elif result == None:
            lemmas_status_code = self.status_code["lemmas"]
            print(f"Lemmas Endpoint request failed: {lemmas_status_code} error.")
        else:
            self.root = result["results"][0]["lexicalEntries"][0]["inflectionOf"][0][
                "text"
            ]

    def call_entries(self):
        """retrieve and return word entry"""
        result = self.call_api("entries")
        if isinstance(result, str):
            print(result)
        elif result == None:
            entries_status_code = self.status_code["entries"]
            print(f"Entries Endpoint request failed: {entries_status_code} Error.")
        else:
            return self.__clean_entries(result)

    def __clean_entries(self, r_json):
        # extract information from r_json and save dict instance
        word_json = {}
        try:
            results = r_json["results"][0]
        except KeyError:
            return word_json
        word_json["word"] = results["word"]
        first_lexical_entry = results["lexicalEntries"][0]
        self.__extract_lexical_entries(
            first_lexical_entry, word_json
        )  # add other entries later
        return word_json

    def __extract_lexical_entries(self, lexical_entry, word_json):
        word_json["lexical_category"] = lexical_entry["lexicalCategory"]["id"]
        entry = lexical_entry["entries"][0]

        # pronunciations
        try:
            pronunciations = entry["pronunciations"][0]
            word_json["audio_link"] = pronunciations["audioFile"]
            word_json["ipa"] = pronunciations["phoneticSpelling"]
        except KeyError:
            pronunciations = ""
            word_json["audio_link"] = ""
            word_json["ipa"] = ""

        # inflection and senses
        senses = entry["senses"][0]
        try:
            inflections = [
                inflection["inflectedForm"] for inflection in entry["inflections"]
            ]
            word_json["inflections"] = ", ".join(inflections)
        except KeyError:
            word_json["inflections"] = ""
        try:
            word_json["senses"] = senses["shortDefinitions"][0]
        except KeyError:
            try:
                word_json["senses"] = senses["definitions"][0]
            except KeyError:
                word_json["senses"] = ""
        try:
            word_json["derivatives"] = lexical_entry["derivatives"][0]["text"]
        except KeyError:
            word_json["derivatives"] = ""