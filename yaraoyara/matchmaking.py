import yara
from git import Repo


# git.Git("/rules").clone("git://github.com/Yara-Rules/rules.git")

def setup_yara():
    indexdict = {
        'malware': '../yaraoyara/repo/malware_index.yar',
        'maldocs': '../yaraoyara/repo/maldocs_index.yar',
        'mobile_malware': '../yaraoyara/repo/mobile_malware_index.yar'}
    rules = yara.compile(filepaths=indexdict)
    rules.save('../yaraoyara/loaded.bin')
    loaded = yara.load('../yaraoyara/loaded.bin')

    return loaded


def matchthis(file):
    loadedrules = yara.load('yaraoyara/loaded.bin')
    matches = loadedrules.match(file)
    print(matches)
    return matches


# matches = rules.match('Keygen.exe')

matchthis('yaraoyara/AutoPico.exe')
# print(matches)
