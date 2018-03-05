# startmeny? character creation?
import time


print('Welcome to Stefan\'s Adventure Game! It\'s a really good game.')
time.sleep(1)
print('Please set the name, age and gender of your character.')
time.sleep(2)

name_tries = 0
name = ''
while name != 'Stig':
    name = input('First, tell me you name')
    if name_tries < 3:
        if name != 'Stig':
            print('Wat')
            name_tries = name_tries + 1
            time.sleep(1)
    else:
        time.sleep(1)
        print('Let\'s just go with Stig, ok?')
        name = 'Stig'
time.sleep(1)


age = 0
while age < 8 or age > 12:
    age = int(input('What is you age?'))
    if age > 12:
        print('That\'s too old! '+str(age)+'? Stig is just a little kid for fucks sake!')
    elif age < 8:
        print('C\'mon, Stig isn\'t that little.')
    else:
        print('Yeah, that sounds about right. But who knows? '
              'Stig is a little orphaned kid. No one really knows how old he is, least of all himself. '
              'And no one cares.')
time.sleep(2)

gender = ''
while gender != 'boy':
    gender = input('So, last but not least, are you a boy, a girl or other?')
    if gender not in ['boy', 'girl', 'other']:
        print('Check your spelling mate.')
    elif gender == 'other':
        print('I was being polite. Other is not a gender.')
    elif gender == 'girl':
        print('C\'mon dude, does Stig sound like a girl\'s name to you?')
    else:
        print('You sure are!')
time.sleep(1)

