import sys

master = 'opensesame'
password = input('Please enter the super secret password:')

attempt = 1
while password != master:
  if attempt > 3:
    sys.exit('Too many invalid attempts')
  password = input('Invalid Password, try again:')
  print('Tries left: {}'.format(3 - attempt))
  attempt += 1

print("Welcome to secret town")
