# dictonary contain keyword and values where user can search value using key 
dictonary= {"Class":"Collection of data member and member functions","Object":"Instance of Class","Array":"Collection of variable having same name and same data type",
            "Constructor":"Having same name as Class name and invoked while calling class"}

word= input("Enter a Word to Search:- ")
print("-----------")
print(word ,"=" ,dictonary[word.capitalize()])