import data

def slack_name(result, file, file2):
  for key in result:
    file.write(str(key['name']) + '\n')
    file2.write(str(key['profile']['email']) + '\n')

with open('name.txt', 'w') as file, open('email.txt', 'w') as file2:
  for i in dir(data):
    if not i.startswith('__'):
      exec(f"slack_name(data.{i}['results'], file, file2)")
