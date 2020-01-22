while True:
  content = '''
  <div class="route">
    <p class="heading">{0}</p>
    <p class="{1}">{2}</p>
    <p class="path">{3}</p>
    <p class="desc">{4}</p>
  '''

  param = '  <p class=param>{0}</p>'

  end = '\n</div>'

  method = str(input("Method: "))
  path = str(input("Path: "))
  heading = str(input("Heading: "))
  desc = str(input("Desc: "))

  params = []

  print("Adding Params... type ':q' when finished entering parameters")
  paramInput = ""
  while True:
    paramInput = str(input("Parameter: "))
    if paramInput == ":q":
      break 
    content += param.format(paramInput) + "\n"


  content = content.format(heading, method, method.upper(), path, desc)
  content = content[:-1]
  content += end

  print(content)
  print("\n\n\n\n\n")