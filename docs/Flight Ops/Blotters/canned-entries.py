import os

raw_entry_file = open("/tower/work/mkwork/docs/Flight Ops/Blotters/canned-entries.txt", "r")


entry_number = "00"
for line in raw_entry_file:
    if line.startswith("## "):
        
        entry_number = "0" + entry_number if entry_number.__len__() == 1 else entry_number
        line_split = line[3:].strip().split("{}")
        entry_title = line_split[0]
        file_name = entry_title.strip().replace(" ", "_").replace("/", "-")
        entry_file = open("/tower/work/mkwork/docs/Flight Ops/Blotters/Canned Entries/" + entry_number + "-" + file_name + ".md", "w")
        try:
            if line_split[1]: entry_file.write("---\ntags:\n  - Mandatory\n---\n\n")
        except IndexError as e:
            print(e)
        entry_file.write("# " + entry_title + "\n")
        entry_number = str(int(entry_number) + 1)

    else:
        entry_file.write(line)

os.system("/tower/work/mkwork/publish")
