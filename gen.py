#!/bin/python3

import csv
import sys

variables = {}
templateFile = open(f'templates/{sys.argv[1]}/template.html')
page = templateFile.read()
templateFile.close()

entryTemplateFile = open(f'templates/{sys.argv[1]}/entryTemplate.html')
entryTemplate = entryTemplateFile.read()[:-1]
entryTemplateFile.close()

with open('config.ini') as configFile:
    index = 1
    for line in configFile:
        line = ''.join(line.split())
        line = line.partition('=')
        if len(line[0]) != 0:
            if line[0][0] == '-':
                variables[line[0]] = line[2]
            else:
                if line[2][0] == '-':
                    page = page.replace(f'${line[0]}$', variables[line[2]])
                else:
                    page = page.replace(f'${line[0]}$', line[2])

with open('entries.csv') as file:
    entries = csv.reader(file)
    for entry in entries:
        if len(entry) != 0:
            page = page.replace('$entry$', entryTemplate)
            if entry[0] == 'blank':
                page = page.replace('$entry_blank$', ' class="blank"')
            else:
                page = page.replace('$entry_blank$', '')
                for i in range(len(entry)):
                    page = page.replace(f'${i}$', ''.join(entry[i].split()))


page = page.replace('$entry$', '')

outputFile = open('home.html', 'w')
outputFile.write(page)
outputFile.close()
