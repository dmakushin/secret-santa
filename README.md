# santas_anonymous
Tool that helps assign roles for classic office game Santa's Anonymous

You should add list of emails of all players into santas_list.json
After that start the tool like

python santa.py --u username --p password --s imap.gmail.com

Where username/password - your credentials for your email and imap.gmail.com 
is example of mail server that can be used.

After that each player in list will get an email with message 
for whom he should prepare a gift

Also tool will create file roles_backup.txt where you can find list of pairs
who prepare a gift and for whom