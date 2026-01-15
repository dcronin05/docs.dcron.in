import os

imgs = os.listdir("docs/files/imgs/")

file = open("docs/.includes/images_test.md", "w")

file.write('<div class="grid cards" markdown>\n\n')

for img in imgs:
    line = f'[![{img}](../files/imgs/{img}){{.tn}}](../files/imgs/{img})' + "\n"
    file.write(line)

file.write('\n</div>')

file.close()
