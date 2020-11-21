from BOOK_Recommender import cosine_sim
import csv
from columnar import columnar
from click import style



User_Book_Name = str(input("Check_BOOK: "))
User_Book_Info = []
#converts the csv to a list
Data_List = []
with open('books.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        Data_List.append(row)

#print(Data_List)
for Book_Data in Data_List:
  
    if Book_Data[1] == User_Book_Name :
        User_Book_Info = Book_Data
        break
else:
    print("NO DATA")
        


#  bookID title	authors	average_rating language_code num_pages	ratings_count	text_reviews_count	publication_date	publisher	summary

    
def Recommendation ():

    Similarity_dict = {}

    for Book_Data in Data_List :
        Id_Check = Book_Data[0]
        Name_Check =  cosine_sim(str(User_Book_Info[1]),str(Book_Data[1]))
        Author_Check =  cosine_sim(str(User_Book_Info[2]),str(Book_Data[2]))
        Rating_Check = Book_Data[3]
        Language_Check = User_Book_Info[4] == Book_Data[4]
        Summary_Check = cosine_sim(str(User_Book_Info[10]),str(Book_Data[10]))
        
        Total = 0
        if Name_Check >= 0.5 :
            Total += Name_Check*50
        if Author_Check >= 0.2:
            Total += Author_Check*30
        if Language_Check == True:
            Total += Language_Check*10
        try:
            Total += float(Rating_Check)*4 + float(Summary_Check)*40
        except:
            Total +=  float(Summary_Check)*40
        Similarity_dict[Book_Data[0]] = [Book_Data[1],Book_Data[2],Book_Data[10],Total]
    
    # Sort Dictionary by value in descending order using lambda function
    sorted_dict = dict( sorted(Similarity_dict.items(),key=lambda item: item[1][-1],reverse=True))


        
    return(sorted_dict)

