import pafy
#This is the documentation for Pafy - a Python library to download YouTube content and retrieve metadata

#Pafy object , argument as url
object = pafy.new("https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q")

#Print title
print("Title : " + object.title)

#print viewcount
print("View Count : " + str(object.viewcount))

#print category
print("Category" + object.category)

#print author name
print("Author : " + object.author)

#length of video
print("Length : " + str(object.length))

#duration
print("Duration : " + object.duration)

#Published on date
print("Published on Date : " + str(object.published))

#likes and dislikes
print("Likes : " + str(object.likes) + "Dislikes : " + str(object.dislikes))

#Ratings
print("Ratings" , int(object.rating))

#read more at http://pythonhosted.org/Pafy/#Pafy.pafy.new
