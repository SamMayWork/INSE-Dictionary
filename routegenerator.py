while True:
  content = '''
  <div class="route">
    <p class="{0}">{1}</p>
    <p class="path">{2}</p>
    <p class="desc">{3}</p>
  '''

  param = '  <p class=param>{0}</p>'

  end = '\n</div>'

  method = str(input("Method: "))
  path = str(input("Path: "))
  desc = str(input("Desc: "))

  params = []

  print("Adding Params... type ':q' when finished entering parameters")
  paramInput = ""
  while True:
    paramInput = str(input("Parameter: "))
    if paramInput == ":q":
      break 
    content += param.format(paramInput) + "\n"


  content = content.format(method, method.upper(), path, desc)
  content = content[:-1]
  content += end

  print(content)
  print("\n\n\n\n\n")