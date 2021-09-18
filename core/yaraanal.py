import os.path
import yara

class YaraAnalysis():

    def __init__(self):

        if not os.path.exists("yara_rules/compiled"):
            self.rules = yara.compile(filepath="yara_rules/index.yar")
            self.rules.save("yara_rules/compiled")

        self.rules = yara.load("yara_rules/compiled")

    def get_matches(self, stream):

        matches = self.rules.match(data=stream)

        return str(matches).strip("][").split(", ")


