a = [
    ["Diye hua options me se Bharat ki rajdhani kon see hai:",["A",["new delhi"]],["B",["maharasta"]],["C",["mumbai"]],["D",["kanpur"]]],
    ["What is the national game of india:",["A",["cricket"]],["B",["football"]],["C",["hockry"]],["D",["table tennis"]]],
    ["the term app in the context of a mobile app is a shortened form of which word",["A",["apple"]],["B",["apparel"]],["C",["apparatus"]],["D",["application"]]],
    ["in which city the golden temple is located ",["A",["patiala"]],["B",["ludhiana"]],["C",["amritsar"]],["D",["chandigarh"]]],
    ["mahabharat ke anusar inme se kon arjun ki patni nhi hai",["A",["subhadra"]],["B",["devika"]],["C",["ulupi"]],["D",["chitrangala"]]]
    ]
life_line = [
            [["A",["new delhi"]],["D",["kanpur"]]],[["A",["cricket"]],["C",["hockey"]]],[["A",["apple"]],["D",["application"]]],
            [["A",["patiala"]],["C",["amritsar"]]],[["B",["devika"]],["D",["Chitrangala"]]]
            ]
r_ans = [["A",["new delhi"]],["C",["hockey"]],["D",["application"]],["C",["amritsar"]],["B",["devika"]]]
price = [10000,200000,1000000,5000000,10000000]
count = 1
n = len(a)
b = input("welcome to kbc game khel suru karne ke liye 'y' or exit karne ke liye 'n' enter kare : ")
if b == "y":
    for i in range(n):
        m = len(a[i])
        for j in range(m):
            if type(a[i][j]) is list:
                print(a[i][j])
            else:
                print("Q.","=",i+1,":-",a[i][j],",\n","And your options are:- ")
        if count<2:
            LfLn = input("Kya aap 50-50 life line use karna chahenge enter 'y' for yes or 'n' for no:- ")
            if LfLn=="y":
                s = len(life_line[i])
                for t in range(s):
                    print(life_line[i][t])
                count = count+1
        else:
            print("Aapke pass koi life line nhi bachi hai ")
        ans = input("Enter the right option in 'CAPITAL' letters: ")
        if ans.upper() ==r_ans[i][0]:
            print("Badhai ho aapka jabab bilkul sahi hai aor aap jit chuke hai rs-",price[i])
        else:
            print("Sorry aap har gye aapka jabab galat hai, sahi jabab hai ",r_ans[i],",\n","Please try again")
            break
        if (i<len(a)-1):
            next = input("Enter 'next' for next qustion or enter 'quit' for quit or exit the game:- ")
            if next != "next":
                print("Thanks for playing kbc and congratulations aap jeet chucke hai",price[i])
                break
        else:
            print("Many many congratulations on your VICTORY!",
             "Aapne sabhi sabalo ke sahi jabab diye hai or aap jeet chuke hai pure: ",price[i],"Rupey",
            ",\n","And again thank you for playing KBC ")
else:
    print("Thank You")
