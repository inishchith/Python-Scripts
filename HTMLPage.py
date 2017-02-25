f=open("Index.html","w")

authorname=input("Enter your name : ")
authorname="<!--author " + authorname +" -->"
f.write(authorname)
startup="""
<!DOCTYPE HTML>
<html lang="en" hackable="off">
<head>
  <title> Website name </title>
  <meta name="robots" content="noindex,nofollow"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
"""
f.write(startup)

#background?
choice=input("Would you like to add background image (y/n) ? ")
if choice=='y':
    link=input("Enter link ")
    sty="<body class=\"body\" oncontextmenu=\"return false\" background=\""+ link +"\">"
    f.write(sty)

#links?
while 1:
    choice=input("Would you like to add links (y/n) ? ")
    if choice=='y':
        link=input("Enter link ")
        title=input("Enter title ")
        link ="<a href= \"http://"+link+ "\"target=\"_blank\">" +title + "</a> <br>"
        f.write(link)
    elif choice=='n' :
        print("Ok Done")
        break
    else :
        print("Invalid choice ")

#images?
while 1:
    choice = input("Would you like to add images (y/n) ? ")
    if choice == 'y':
        link = input("Enter link ")
        link = "<img src= \"" + link + "\"/> <br>"
        f.write(link)
    elif choice == 'n':
        print("Ok Done")
        break
    else:
        print("Invalid choice ")

#stuff
inp=input("Would you like to add some gifs (y/n) ?")
if inp=='y':
    ext= """
<br> <br>
<br> <br>
<br> <br>
<br> <br>
<marquee behavior="scroll" direction="left"> <img src="http://www.allgifs.com/wp-content/uploads/2013/08/tumblr_mrmi90oEHD1srth6oo1_400.gif" width="300" height="300" alt="<3">
</marquee>"""
    f.write(ext)

#end
end="""
</body>
</html>
"""
f.write(end)