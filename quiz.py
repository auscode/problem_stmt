def gk():
    questions = [
        {"question": "Who is known as the 'Father of the Nation' in India?",
         "options": {"a": "Jawaharlal Nehru", "b": "Subhas Chandra Bose", "c": "Mahatma Gandhi", "d": "Bhagat Singh"},
         "answer": "c"},
        {"question": "What is the capital city of France?",
         "options": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome"},
         "answer": "c"},
        {"question": "Which planet is known as the Red Planet?",
         "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
         "answer": "b"},
        {"question": "Who wrote the play 'Romeo and Juliet'?",
         "options": {"a": "Charles Dickens", "b": "J.K. Rowling", "c": "William Shakespeare", "d": "Mark Twain"},
         "answer": "c"},
        {"question": "What is the largest ocean on Earth?",
         "options": {"a": "Atlantic Ocean", "b": "Indian Ocean", "c": "Arctic Ocean", "d": "Pacific Ocean"},
         "answer": "d"},
        {"question": "Who painted the Mona Lisa?",
         "options": {"a": "Vincent van Gogh", "b": "Pablo Picasso", "c": "Leonardo da Vinci", "d": "Claude Monet"},
         "answer": "c"},
        {"question": "What is the smallest country in the world by land area?",
         "options": {"a": "Monaco", "b": "Vatican City", "c": "San Marino", "d": "Liechtenstein"},
         "answer": "b"},
        {"question": "Who was the first person to walk on the moon?",
         "options": {"a": "Yuri Gagarin", "b": "Buzz Aldrin", "c": "Neil Armstrong", "d": "Michael Collins"},
         "answer": "c"},
        {"question": "What is the longest river in the world?",
         "options": {"a": "Amazon River", "b": "Yangtze River", "c": "Nile River", "d": "Mississippi River"},
         "answer": "c"},
        {"question": "Which country is known as the Land of the Rising Sun?",
         "options": {"a": "China", "b": "South Korea", "c": "Japan", "d": "Thailand"},
         "answer": "c"}
    ]
    return questions

def science():
    questions = [
        {"question": "What is the chemical symbol for water?",
         "options": {"a": "O2", "b": "H2O", "c": "CO2", "d": "NaCl"},
         "answer": "b"},
        {"question": "What force keeps us grounded on Earth?",
         "options": {"a": "Magnetism", "b": "Friction", "c": "Gravity", "d": "Inertia"},
         "answer": "c"},
        {"question": "What is the powerhouse of the cell?",
         "options": {"a": "Nucleus", "b": "Ribosome", "c": "Mitochondria", "d": "Chloroplast"},
         "answer": "c"},
        {"question": "What is the speed of light in a vacuum?",
         "options": {"a": "300,000 km/s", "b": "150,000 km/s", "c": "450,000 km/s", "d": "600,000 km/s"},
         "answer": "a"},
        {"question": "What is the most abundant gas in Earth's atmosphere?",
         "options": {"a": "Oxygen", "b": "Carbon Dioxide", "c": "Nitrogen", "d": "Hydrogen"},
         "answer": "c"},
        {"question": "What is the process by which plants make their food?",
         "options": {"a": "Respiration", "b": "Photosynthesis", "c": "Digestion", "d": "Fermentation"},
         "answer": "b"},
        {"question": "Who proposed the theory of relativity?",
         "options": {"a": "Isaac Newton", "b": "Albert Einstein", "c": "Galileo Galilei", "d": "Niels Bohr"},
         "answer": "b"},
        {"question": "What is the basic unit of life?",
         "options": {"a": "Atom", "b": "Molecule", "c": "Cell", "d": "Organ"},
         "answer": "c"},
        {"question": "What is the hardest natural substance on Earth?",
         "options": {"a": "Gold", "b": "Iron", "c": "Diamond", "d": "Quartz"},
         "answer": "c"},
        {"question": "What is the main gas found in the sun?",
         "options": {"a": "Oxygen", "b": "Helium", "c": "Hydrogen", "d": "Carbon"},
         "answer": "c"}
    ]
    return questions

def history():
    questions = [
        {"question": "Who was the first President of the United States?",
         "options": {"a": "Thomas Jefferson", "b": "John Adams", "c": "George Washington", "d": "James Madison"},
         "answer": "c"},
        {"question": "What year did World War II end?",
         "options": {"a": "1942", "b": "1945", "c": "1948", "d": "1950"},
         "answer": "b"},
        {"question": "Who was the ancient Egyptian queen known for her beauty and political acumen?",
         "options": {"a": "Nefertiti", "b": "Hatshepsut", "c": "Cleopatra", "d": "Isis"},
         "answer": "c"},
        {"question": "What was the name of the ship that carried the Pilgrims to America in 1620?",
         "options": {"a": "Santa Maria", "b": "Mayflower", "c": "Endeavour", "d": "Beagle"},
         "answer": "b"},
        {"question": "Who was the leader of the Soviet Union during World War II?",
         "options": {"a": "Vladimir Lenin", "b": "Joseph Stalin", "c": "Nikita Khrushchev", "d": "Leonid Brezhnev"},
         "answer": "b"},
        {"question": "What ancient civilization built the Machu Picchu?",
         "options": {"a": "Aztec", "b": "Maya", "c": "Inca", "d": "Olmec"},
         "answer": "c"},
        {"question": "What was the name of the first successful English colony in America?",
         "options": {"a": "Roanoke", "b": "Jamestown", "c": "Plymouth", "d": "Salem"},
         "answer": "b"},
        {"question": "Who was the famous British Prime Minister during World War II?",
         "options": {"a": "Neville Chamberlain", "b": "Winston Churchill", "c": "Clement Attlee", "d": "Margaret Thatcher"},
         "answer": "b"},
        {"question": "What was the main cause of the American Civil War?",
         "options": {"a": "Taxation", "b": "Slavery", "c": "Territorial Expansion", "d": "Religious Freedom"},
         "answer": "b"},
        {"question": "Who was the first emperor of China?",
         "options": {"a": "Liu Bang", "b": "Qin Shi Huang", "c": "Kublai Khan", "d": "Sun Tzu"},
         "answer": "b"}
    ]
    return questions


def game(choice):
    questions = []
    ques=0
    score = 0
    if choice=="1":
        questions = gk()
    elif choice =="2":
        questions = science()
    elif choice=="3":
        questions = history()
    else:
        print("Invalid Input Try again!")
    
    if len(questions)<1:
        return "Invalid Input Try again!"
    else:
        for i,k in enumerate(questions):
            print(f"Question {i+1}:{k['question']}")
            print(f"A:{k['options']['a']}")
            print(f"B:{k['options']['b']}")
            print(f"C:{k['options']['c']}")
            print(f"D:{k['options']['d']}")
            ans  = input("Enter your answer (A/B/C/D): ")
            ques+=1
            if ans.lower() == k['answer']:
                print("Correct!\n")
                score +=1
            else:
                print(f"Wrong! The correct answer is {k['answer']}\n")
    
    print(f"Final Score: {score}/{ques}")
    print("Thank you for playing!")
    print("\nWanna Play Again?")
    quizfxn()
    

def quizfxn():
    print("Select a category:")
    print("1. General Knowledge")
    print("2. Science")
    print("3. History")
    
    choice = input("Enter your choice: ")
    game(choice)


def main_menu():
    while True:
        print("===== Quiz Application =====")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            quizfxn()
        elif choice =="2":
            print("Goodbye!")
        else:
            print("Invalid Input\nGoodBye!")
        
if __name__ == "__main__":
    main_menu()
