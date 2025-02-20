import random
import threading
import time
import sys

questions_dict = {
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the smallest country in the world?": "Vatican City",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the chemical symbol for gold?": "Au",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the capital of Australia?": "Canberra",
    "What is the longest river in the world?": "Nile",
    "Who developed the theory of relativity?": "Albert Einstein",
    "What is the hardest natural substance on Earth?": "Diamond",
    "What is the capital of Japan?": "Tokyo",
    "Who is known as the father of computers?": "Charles Babbage",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the capital of France?": "Paris",
    "Who wrote '1984'?": "George Orwell",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Sistine Chapel ceiling?": "Michelangelo",
    "What is the capital of Canada?": "Ottawa",
    "What is the largest desert in the world?": "Sahara",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the capital of Italy?": "Rome",
    "Who wrote 'Pride and Prejudice'?": "Jane Austen",
    "What is the chemical symbol for oxygen?": "O",
    "Who painted 'Starry Night'?": "Vincent van Gogh",
    "What is the capital of Germany?": "Berlin",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who discovered America?": "Christopher Columbus",
    "What is the capital of Russia?": "Moscow",
    "Who wrote 'The Great Gatsby'?": "F. Scott Fitzgerald",
    "What is the chemical symbol for iron?": "Fe",
    "Who painted 'The Last Supper'?": "Leonardo da Vinci",
    "What is the capital of China?": "Beijing",
    "What is the largest continent?": "Asia",
    "Who discovered gravity?": "Isaac Newton",
    "What is the capital of India?": "New Delhi",
    "Who wrote 'Moby-Dick'?": "Herman Melville",
    "What is the chemical symbol for sodium?": "Na",
    "Who painted 'The Persistence of Memory'?": "Salvador Dalí",
    "What is the capital of Brazil?": "Brasília",
    "What is the smallest planet in our solar system?": "Mercury",
    "Who wrote 'The Odyssey'?": "Homer",
    "What is the chemical symbol for potassium?": "K",
    "Who painted 'Guernica'?": "Pablo Picasso",
    "What is the capital of Mexico?": "Mexico City",
    "What is the largest island in the world?": "Greenland",
    "Who discovered the structure of DNA?": "James Watson and Francis Crick",
    "What is the capital of Egypt?": "Cairo",
    "Who wrote 'War and Peace'?": "Leo Tolstoy",
    "What is the chemical symbol for carbon?": "C",
    "Who painted 'The Birth of Venus'?": "Sandro Botticelli",
    "What is the capital of Spain?": "Madrid",
    "What is the largest bone in the human body?": "Femur",
    "Who discovered radioactivity?": "Henri Becquerel",
    "What is the capital of Argentina?": "Buenos Aires",
    "Who wrote 'The Catcher in the Rye'?": "J.D. Salinger",
    "What is the chemical symbol for nitrogen?": "N",
    "Who painted 'The Scream'?": "Edvard Munch",
    "What is the capital of South Korea?": "Seoul",
    "What is the largest organ in the human body?": "Skin",
    "Who discovered the electron?": "J.J. Thomson",
    "What is the capital of Turkey?": "Ankara",
    "Who wrote 'The Hobbit'?": "J.R.R. Tolkien",
    "What is the chemical symbol for calcium?": "Ca",
    "Who painted 'The Night Watch'?": "Rembrandt",
    "What is the capital of Greece?": "Athens",
    "What is the largest land animal?": "African Elephant",
    "Who discovered the law of motion?": "Isaac Newton",
    "What is the capital of Portugal?": "Lisbon",
    "Who wrote 'The Divine Comedy'?": "Dante Alighieri",
    "What is the chemical symbol for chlorine?": "Cl",
    "Who painted 'The School of Athens'?": "Raphael",
    "What is the capital of the Netherlands?": "Amsterdam",
    "What is the largest bird in the world?": "Ostrich",
    "Who discovered the polio vaccine?": "Jonas Salk",
    "What is the capital of Sweden?": "Stockholm",
    "Who wrote 'The Brothers Karamazov'?": "Fyodor Dostoevsky",
    "What is the chemical symbol for magnesium?": "Mg",
    "Who painted 'The Kiss'?": "Gustav Klimt",
    "What is the capital of Norway?": "Oslo",
    "What is the largest fish in the world?": "Whale Shark",
    "Who discovered the circulation of blood?": "William Harvey",
    "What is the capital of Finland?": "Helsinki",
    "Who wrote 'The Iliad'?": "Homer",
    "What is the chemical symbol for phosphorus?": "P",
    "Who painted 'The Garden of Earthly Delights'?": "Hieronymus Bosch",
    "What is the capital of Denmark?": "Copenhagen",
    "What is the largest reptile in the world?": "Saltwater Crocodile",
    "Who discovered the neutron?": "James Chadwick",
    "What is the capital of Poland?": "Warsaw",
    "Who wrote 'The Picture of Dorian Gray'?": "Oscar Wilde",
    "What is the chemical symbol for sulfur?": "S",
    "Who painted 'The Arnolfini Portrait'?": "Jan van Eyck",
    "What is the capital of Hungary?": "Budapest",
    "What is the largest amphibian in the world?": "Chinese Giant Salamander",
    "Who discovered the proton?": "Ernest Rutherford",
    "What is the capital of Austria?": "Vienna",
    "Who wrote 'The Count of Monte Cristo'?": "Alexandre Dumas",
    "What is the chemical symbol for zinc?": "Zn",
    "Who painted 'The Hay Wain'?": "John Constable",
    "What is the capital of Belgium?": "Brussels",
    "What is the largest invertebrate in the world?": "Colossal Squid",
    "Who discovered the X-ray?": "Wilhelm Conrad Roentgen",
    "What is the capital of Switzerland?": "Bern",
    "Who wrote 'The Three Musketeers'?": "Alexandre Dumas",
    "What is the chemical symbol for copper?": "Cu",
    "Who painted 'The Blue Boy'?": "Thomas Gainsborough",
    "What is the capital of Ireland?": "Dublin",
    "What is the largest carnivore on land?": "Polar Bear",
    "Who discovered the law of universal gravitation?": "Isaac Newton",
    "What is the capital of Scotland?": "Edinburgh",
    "Who wrote 'The Hunchback of Notre-Dame'?": "Victor Hugo",
    "What is the chemical symbol for silver?": "Ag",
    "Who painted 'The Swing'?": "Jean-Honoré Fragonard",
    "What is the capital of Wales?": "Cardiff",
    "What is the largest rodent in the world?": "Capybara",
    "Who discovered the law of conservation of mass?": "Antoine Lavoisier",
    "What is the capital of Northern Ireland?": "Belfast",
    "Who wrote 'Les Misérables'?": "Victor Hugo",
    "What is the chemical symbol for lead?": "Pb",
    "Who painted 'The Death of Marat'?": "Jacques-Louis David",
    "What is the capital of New Zealand?": "Wellington",
    "What is the largest marsupial in the world?": "Red Kangaroo",
    "Who discovered the law of definite proportions?": "Joseph Proust",
    "What is the capital of South Africa?": "Pretoria",
    "Who wrote 'The Old Man and the Sea'?": "Ernest Hemingway",
    "What is the chemical symbol for mercury?": "Hg",
    "Who painted 'The Raft of the Medusa'?": "Théodore Géricault",
    "What is the capital of Nigeria?": "Abuja",
    "What is the largest primate in the world?": "Eastern Gorilla",
    "Who discovered the law of multiple proportions?": "John Dalton",
    "What is the capital of Kenya?": "Nairobi",
    "Who wrote 'The Stranger'?": "Albert Camus",
    "What is the chemical symbol for tin?": "Sn",
    "Who painted 'The Fighting Temeraire'?": "J.M.W. Turner",
    "What is the capital of Ghana?": "Accra",
    "What is the largest bony fish in the world?": "Ocean Sunfish",
    "Who discovered the law of electrolysis?": "Michael Faraday",
    "What is the capital of Ethiopia?": "Addis Ababa",
    "Who wrote 'The Metamorphosis'?": "Franz Kafka",
    "What is the chemical symbol for platinum?": "Pt",
    "Who painted 'The Night Café'?": "Vincent van Gogh",
    "What is the capital of Uganda?": "Kampala",
    "What is the largest arthropod in the world?": "Japanese Spider Crab",
    "Who discovered the law of electromagnetic induction?": "Michael Faraday",
    "What is the capital of Tanzania?": "Dodoma",
    "Who wrote 'The Trial'?": "Franz Kafka",
    "What is the chemical symbol for gold?": "Au",
    "Who painted 'The Yellow House'?": "Vincent van Gogh",
    "What is the capital of Zimbabwe?": "Harare",
    "What is the largest echinoderm in the world?": "Sunflower Sea Star",
    "Who discovered the law of thermodynamics?": "Rudolf Clausius",
    "What is the capital of Zambia?": "Lusaka",
    "Who wrote 'The Castle'?": "Franz Kafka",
    "What is the chemical symbol for uranium?": "U",
    "Who painted 'The Potato Eaters'?": "Vincent van Gogh",
    "What is the capital of Botswana?": "Gaborone",
    "What is the largest cephalopod in the world?": "Giant Squid"}

questions = list(questions_dict.keys())
answers = list(questions_dict.values())

def countdown_timer(stop_event, duration=30):
    """Simple countdown timer that runs for 'duration' seconds or until stop_event is set."""
    for i in range(duration, 0, -1):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{i:2}")  # Just print the countdown number
        sys.stdout.flush()
        time.sleep(1)
    if not stop_event.is_set():
        sys.stdout.write("\r 0\n")
        sys.stdout.flush()
        print("Time's up!")

def input_with_timeout(prompt, timeout, stop_event):
    """Get user input with a timeout."""
    def get_input():
        nonlocal answer
        print(f"{' ' * 10}{prompt}", end='', flush=True)  # Shift prompt to the right
        answer = input()
        stop_event.set()

    answer = None
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    
    input_thread.join(timeout)
    
    if not stop_event.is_set():
        stop_event.set()

    return answer

def ask_question(total, stop_event):
    """Ask a random question and check user's answer."""
    question = random.choice(questions)
    correct_answer = questions_dict[question]

    # Ensure unique incorrect options
    options = random.sample([ans for ans in answers if ans != correct_answer], 3)
    options.append(correct_answer)
    random.shuffle(options)

    print("\n" + question)
    option_labels = ['a', 'b', 'c', 'd']
    for i, option in enumerate(options):
        print(f"{option_labels[i]}. {option}")

    # Start the timer in a separate thread
    stop_event.clear()
    timer_thread = threading.Thread(target=countdown_timer, args=(stop_event, 10))  # 10 sec for quick test
    timer_thread.start()

    # Get the user's answer with a timeout
    answer = input_with_timeout("Your answer (a/b/c/d): ", 10, stop_event)
    
    # Ensure the timer thread stops after input is received or time runs out
    stop_event.set()
    timer_thread.join()

    if answer and answer.lower() in 'abcd':
        selected_option = options['abcd'.index(answer.lower())]
        if selected_option == correct_answer:
            print("✅ Correct!\n")
            total.append(1)
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}.\n")
    else:
        print(f"⏳ Time's up! The correct answer is {correct_answer}.\n")

if __name__ == "__main__":
    stop_event = threading.Event()
    
    while True:
        total = []
        for _ in range(5):  # Reduced for testing
            ask_question(total, stop_event)
        
        print(f"\n🎯 Total correct answers: {len(total)} / 5")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
