import os


versions=[
  'master',
  '1.x', 
  '2.x', 
  '3.x', 
]

for v in versions:
  dir = 'resources/docs/' + v;
  if os.path.isdir(dir):
    print('pull ' + v);
    os.system("cd " + dir + " && git pull") 
  else:
    print('create ' + v);
    os.system("git clone --single-branch --branch '" + v + "' git@github.com:fansheng0594/test.doc.git " + dir);