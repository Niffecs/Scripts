import filecmp
import os
import shutil
from os import listdir
from os.path import isfile, join

import shortuuid

import helper

# Create Session ID
id = shortuuid.ShortUUID().random(length=6)

# Legt einen Temp Folder an
os.mkdir('tmp_'+id)

# Liest den Ordner ein :)
onlyfiles = [f for f in listdir(
    str(os.getcwd())) if isfile(join(str(os.getcwd()), f))]
print("Files:", onlyfiles, "\n")


# Erlaubte Datei Typen
datatype = ["png", "jpg", "PNG", "JPG"]

# Test Output
print("Types", datatype, "\n")


# Filtern der Daten
data = []
for runner in onlyfiles:
    if runner[-3::] in datatype:
        data.append(runner)

# Test Output
print("Data", data, "\n")

# Läuft alle Datein durch
for base in data:
    for test in data:
        if not base.__eq__(test):
            if filecmp.cmp(base, test):
                # Test Layer
                print(f"{base} <--> {test}")
                shutil.move(helper.os_bindings(
                    f"{os.getcwd()}/{test}"), helper.os_bindings(f"{os.getcwd()}/tmp_{id}/{test}"))
                new_data = []
                for runer in data:
                    if runner != test:
                        new_data.append(runer)
                data = new_data
