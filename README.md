[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/dmakushin/santas-anonymous.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/dmakushin/santas-anonymous/context:python)

# secret-santa
Tool that helps assign roles for classic office game Secret Santa

You should add list of emails of all players into santas_list.json. Only one email per line.
After that start the tool like

`python santa.py --u username --p password --s imap.gmail.com`

Where username/password - your credentials for your email and imap.gmail.com 
is example of mail server which might be used.

After that each player in list will receive an email with message 
for whom he should prepare a gift

Also tool will create file roles_backup.txt where you can find list of pairs
who prepare a gift and for whom
