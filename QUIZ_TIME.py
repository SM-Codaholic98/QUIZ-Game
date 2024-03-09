import random, ascii_magic, pyttsx3

a="""Who scored India's first Test centuary and was also the
only bowler to dismiss sir Don Bradman hit wicket ?
     (a) Vinoo Mankad  (b) Lala Amarnath  (c) Vijay Hazare  (d) Vijay Merchant"""
b="""Who are the only two Indian batsmen to bat on all 5 days of a Test match ?
      (a) Ravi Shastri & M.L. jaisimha  (b) Sachin Tendulkar & Sourav Ganguly  
      (c) Rahul Dravid & V.V.S. Laxman  (d) Virender Sehwag & Gautam Gambhir"""
c="""Which kebab shares its name with a small hamlet on the outkirts of lucknow ?
     (a) Nehari  (b) Kakori  (c) Patili  (d) Nadroo"""
d="""which of these gets its name from the portuguese words for 'wine' and 'garlic' ?
     (a) Jalfrezi  (b) Vindaloo  (c) Do pyaza  (d) Bhuna Gosht"""
e="""With which film did Shreya Ghoshal make her Bollywood debut as a playback singer ?
     (a) Parineeta  (b) Devdas  (c) Jab We Met  (d) Kal Ho Naa Ho"""
f="""Who compossed and recorded songs written by Atal Bihari Vajpayee in two albums, Nayi Disha and Samvedna ?
     (a) A.R. Rahman  (b) Shankar Mahadevan  (c) Jagjit Singh  (d) Pankaj Udhas"""
g="""A.R. Rahman composed 'ginga', an Oscar-nominated song, to celebrate the legacy of which sportsperson ?
     (a) Diego Maradona  (b) Muhammad Ali  (c) Pele  (d) Don Bradman"""
h="""Which counrty does the Radcliffe Line separate India from ?
     (a) Bangladesh  (b) Nepal  (c) Bhutan  (d) Pakistan"""
i="""Which of the following separates little Andaman from the Nicobar Islands ?
     (a) Zero Mile River  (b) Ten Degree Channel  (c) Hundred Furlong Canal  (d) Thousand Yard Bridge"""
j="""The Siliguri Corridor-a narrow strip of land that connects the Indian mainland 
with the outlying border states of the Northeast-is also known as the Eastern...
     (a) Duck's Neck  (b) Ckicken's Neck  (c) Sparrow's Neck  (d) Turkey's Neck"""
k="""The former name of which Indian city is common with a trophy in
rugby contested for annually between England and Scotland ?
     (a) Bombay  (b) Madras  (c) Bangalore  (d) Calcutta"""
l="""Who said: 'Bombs and pistols do not make a revolution.The sword 
of revolution is sharpened on the whetting-stone of ideas' ?
     (a) Mother Teresa  (b) Mahatma Gandhi  (c) Vikram Sarabhai  (d) Bhagat Singh"""
m="""whose words are these: 'An America economist has predict that in the next century 
India will be an economic superpower. I want India to be a happy country.' ? 
     (a) Mahatma Gandhi  (b) Atal Bihari Vajpayee  (c) Mother Teresa  (d) J.R.D. Tata"""
n="""According to A.P.J. Abdul Kalam, what is a continuous process and not an accident
     (a) Excellence  (b) Prosperity  (c) Happiness  (d) Growth"""
o="""Which of these is the state animal of Jammu and Kashmir ?
     (a) Mithun  (b) Hangul  (c) Giant squirrel  (d) One-horned rhinoceros"""
p="""What is the common name of Ailurus fulgens found in Sikkim, West Bengal, Meghalaya and Arunachal Pradesh ?
     (a) Indian pangolin  (b) Nilgiri thar  (c) Snow leopard  (d) Red panda"""
q="""In India, what is produced from Chanthangi and Chegu breeds of goats ?
     (a) Pashmina  (b) Mohair  (c) Merino wool  (d) Shahtoosh"""
r="""Who was the prime minister of United Kingdom when India became independent ?
     (a) Clement Attlee  (b) Winston Churchill  (c) Harold Macmillan  (d) Neville Chamberlain"""
s="""On whose birth anniversary is the National Education Day celebrated in India ?
     (a) Maulana Abul Kalam Azad  (b) Vallabhbhai  (c) S.Radhakrishnan  (d) Lala Lajpat Rai"""
t="""Who was defeated by the brave Rajput chiefs of northern India headed 
by Prithvi Raj Chauhan in the First Battle of Tarain in AD 1191 ?
     (a) Qutb ud-Din Aibak  (b) Muhammad Ghori  (c) Ghyasuddin Tughlaq  (d) Khizar Khan"""

d={a:'b',b:'a',c:'b',d:'b',e:'b',f:'c',g:'c',h:'d',i:'b',j:'b',k:'d',l:'d',m:'d',n:'a',o:'b',p:'d',q:'a',r:'a',s:'a',t:'b'}
key=d.keys()

def QUIZ_GAME(w):
    sum=0
    z=0
    for x in range(w):
        x=random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t])
        for y in key:
            if y==x:
                print()
                print(y)
                ch=input("Enter your choice: ").lower()
                if ch==d[y]:
                    print("Correct")
                    #print()
                    sum=sum+1
                else:
                    print("Wrong")
                    print()
                    z=z+1
    print()
    print("Total number of correct answer given by you: ",sum)
    print("Total number of wrong answer given by you: ",z)
    print()
    totsc=(sum*2)-(z*(1))
    print("Your Total Score is: ",totsc)
    if totsc>=3:
        print("CONGRATS! You won the match, keep it up")
    else:
        print("ALAS! You loose the match, try for the next time")


def main():
    ans='y'
    while ans.lower()=='y':
         print()
         output = ascii_magic.from_image_file("quiz-comic-pop-art-style-quiz-brainy-game-word-vector-illustration-design_180786-81.jpg", columns=170, char='@')
         ascii_magic.to_terminal(output)
         print()
         output = ascii_magic.from_image_file("Quiz-Games.png", columns=110, char='@')
         ascii_magic.to_terminal(output)
         print()
         
         text_speech = pyttsx3.init()
         a = "welcome to quiz game"
         text_speech.setProperty("rate", 110)
         text_speech.say(a)
         text_speech.runAndWait()
         
         print("""NOTE: 1) Each questions carry 2(two) marks
      2) For entering wrong choice you will get -1(minus one)
      3) For winning the game minimum you have to get 3(three) marks otherwise you will loose the game""")
         print()
         w1=int(input("For how many questions you want to play the QUIZ GAME: "))
         print()
         
         output = ascii_magic.from_image_file("5692030.png", columns=100, char='@')
         ascii_magic.to_terminal(output)
         
         print()
         QUIZ_GAME(w1)
         print()
         
         output = ascii_magic.from_image_file("1153441.png", columns=150, char='@')
         ascii_magic.to_terminal(output)
         print()
         
         text_speech = pyttsx3.init()
         a = "thank you for playing quiz"
         text_speech.setProperty("rate", 110)
         text_speech.say(a)
         text_speech.runAndWait()
         
         output = ascii_magic.from_image_file("how-to-respond-to-thank-you.webp", columns=150, char='@')
         ascii_magic.to_terminal(output)
         
         print()
         ans=input("Press 'y' or 'Y' to play again or press any other to quit the game: ")
         print()

if __name__=='__main__':
    main()