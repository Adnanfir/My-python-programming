film={
    "Finding Dory":[13,5]
    ,"Bourne":[18,5]
    ,"Star Wars":[13,5]
    ,"The Accountant":[14,5]
    ,"Doctor Strange":[15,5]  
    
}
while True:
    print("Welcome to the cinema simultor")
    print("1. Show all Movies")
    print("2. Book a ticket")
    print("3. Exit")
    print("""4.Add or remove movies 'for Admin's Only' """)
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Available movies:")
        for movie in film:
            print(movie)
    elif choice==2:
        movie_name=input("Enter the nanme of the movie:").title().strip()
        if movie_name in film:
            age=int(input("Enter your age:"))
        if age>=film[movie_name][0]:
            print("You are eligible to watch this movie")
            ticket=int(input("Enter the number of tickets you want to book:"))
            if ticket<=film[movie_name][1]:
                print("Your tickets have been booked successfully")
                film[movie_name][1]-=ticket
            else:
                print("Sorry, not enough tickets available")       
        else:
            print("You are not eligible to watch this movie")       
    elif choice==4:
        print("Password required first")
        password=input("Enter the password:")
        if password=="admin":
            print("Welcome Admin")
            choice2=int(input("1.Add movie\n2.Remove movie\n3.Exit"))
            if choice2==1:
                movie_name=input("Enter the name of the movie:").title().strip()
                age=int(input("Enter the age rating:"))
                ticket=int(input("Enter the number of tickets available:"))
                film[movie_name]=[age,ticket]
                print("Movie added successfully")
            elif choice2==2:
                movie_name=input("Enter the name of the movie to remove:").title().strip()
                if movie_name in film:
                    del film[movie_name]
                    print("Movie removed successfully")
                else:
                    print("Movie not found")
            elif choice2==3:
                print("Exiting admin mode")
    
    elif choice==3:
        print("Thank you for using the cinema simulator")
        
    else:
        print("Invalid choice, please try again")  
        break       