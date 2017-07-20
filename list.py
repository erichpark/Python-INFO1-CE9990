"""
list.py

Eric Park
INFO1-CE9990 Section 2
Homework for July 13, 2017

James Bond Actors and Their 007 Movies
"""


import sys

Connery = [
    ["Dr. No",                                  1962,  16_067_035.00,
        ["Sean Connery", "Ursula Andress", "Joseph Wiseman", "Jack Lord"]
    ],

    ["From Russia With Love",                   1963,  24_800_000.00,
        ["Sean Connery", "Pedro Armendáriz", "Lotte Lenya", "Robert Shaw", "Bernard Lee", "Daniela Bianchi"]
    ],

    ["Goldfinger",                              1964,  51_100_000.00,
        ["Sean Connery", "Honor Blackman", "Gert Fröbe"]
    ],

    ["Thunderball",                             1965,  63_600_000.00,
        ["Sean Connery", "Claudine Auger", "Adolfo Celi", "Luciana Paluzzi", "Rik Van Nutter"]
    ],

    ["You Only Live Twice",                     1967,  43_100_000.00,
        ["Sean Connery", "Akiko Wakabayashi", "Mie Hama", "Tetsurō Tamba"]
    ],

    ["Diamonds are Forever",                    1971,  43_800_000.00,
        ["Sean Connery", "Jill St. John", "Charles Gray", "Lana Wood", "Jimmy Dean", "Bruce Cabot"]
    ],

    ["Never Say Never Again",                   1983,  55_500_000.00,
        ["Sean Connery", "Klaus Maria Brandauer", "Max von Sydow", "Barbara Carrera", "Kim Basinger"]
    ]      
]


Niven = [
     ["Casino Royale",                          1967,  41_700_000.00,
        ["David Niven", "Peter Sellers", "Ursula Andress", "Woody Allen", "Joanna Pettet", "Orson Welles", "Daliah Lavi"]
     ]
]


Lazenby = [
     ["On Her Majesty's Secret Service",        1969,  22_800_000.00,
        ["George Lazenby", "Diana Rigg", "Telly Savalas", "Gabriele Ferzetti", "Ilse Steppat"]
     ]
]


Moore = [
     ["Live and Let Die",                       1973,  35_400_000.00,
        ["Roger Moore", "Yaphet Kotto", "Jane Seymour"]
     ],

     ["The Man with the Golden Gun",            1974,  21_000_000.00,
        ["Roger Moore", "Christopher Lee", "Britt Ekland", "Maud Adams", "Hervé Villechaize"]
     ],

     ["The Spy Who Loved Me",                   1977,  46_800_000.00,
        ["Roger Moore", "Barbara Bach", "Curd Jürgens", "Richard Kiel", "Caroline Munro"]
     ],

     ["Moonraker",                              1979,  62_700_000.00,
        ["Roger Moore", "Lois Chiles", "Michael Lonsdale", "Richard Kiel", "Corinne Cléry"]
     ],

     ["For Your Eyes Only",                     1981,  62_300_000.00,
        ["Roger Moore", "Carole Bouquet", "Topol", "Lynn-Holly Johnson", "Julian Glover", "Cassandra Harris"]
     ],

     ["Octopussy",                              1983,  67_900_000.00,
        ["Roger Moore", "Maud Adams", "Louis Jourdan", "Kristina Wayborn"]
     ],

     ["A View to a Kill",                       1985,  50_300_000.00,
        ["Roger Moore", "Christopher Walken", "Tanya Roberts", "Grace Jones"],
     ]
]


Dalton = [
     ["The Living Daylights",                   1987,  51_185_897.00,
         ["Timothy Dalton", "Maryam d'Abo", "Jeroen Krabbé"]
     ],

     ["License to Kill",                        1989,  34_667_015.00,
         ["Timothy Dalton", "Carey Lowell", "Robert Davi", "Talisa Soto", "Anthony Zerbe"]
     ]
]


Brosnan = [
     ["GoldenEye",                              1995,  106_635_996.00,
         ["Pierce Brosnan", "Sean Bean", "Izabella Scorupco", "Famke Janssen"]
     ],

     ["Tomorrow Never Dies",                    1997,  125_332_007.00,
         ["Pierce Brosnan", "Jonathan Pryce", "Michelle Yeoh", "Teri Hatcher"]
     ],

     ["The World is Not Enough",                1999,  126_930_660.00,
         ["Pierce Brosnan", "Sophie Marceau", "Robert Carlyle", "Denise Richards"]
     ],

     ["Die Another Day",                        2002,  160_201_106.00,
         ["Pierce Brosnan", "Halle Berry", "Toby Stephens", "Rosamund Pike", "Rick Yune"]
     ]
]


Craig = [
     ["Casino Royale",                          2006,  167_007_184.00,
        ["Daniel Craig", "Eva Green", "Mads Mikkelsen", "Judi Dench", "Jeffrey Wright"]
     ],

     ["Quantum of Solace",                      2008,  168_368_427.00,
        ["Daniel Craig", "Olga Kurylenko", "Mathieu Amalric"]
     ],

     ["Skyfall",                                2012,  304_360_277.00,
        ["Daniel Craig", "Judi Dench", "Javier Bardem", "Ralph Fiennes", "Naomie Harris", "Bérénice Marlohe"]
     ],

     ["Spectre",                                2015,  200_074_175.00,
        ["Daniel Craig", "Christoph Waltz", "Léa Seydoux", "Ralph Fiennes", "Monica Bellucci"]
     ]
]

bonds = [
    Connery, #0
    Niven,   #1
    Lazenby, #2
    Moore,   #3
    Dalton,  #4
    Brosnan, #5
    Craig,   #6
]

print("Enter")
for i, bond in enumerate(bonds):
    print("'", i, "' ", "for ", bond[0][3][0], sep = "")

f = """\
Title: {}
Year: {}
Box office: ${:,.2f}
Starring: """

while True:

    while True:
        try:
            actor = input()
        except EOFError:
            sys.exit(0)

        try:
            actor = int(actor)
        except ValueError:
            print()
            print("Sorry,", actor, "is not a valid selection. Please try again.")
            print()
            continue   #Go back up to the second "while"

        if 0 <= actor and actor < len(bonds):
            break;

        print()
        print("Sorry,", actor, "is not a valid selection. Please try again.")
        print()

    print() #Skip a line

    for movie in bonds[actor]:
        print(f.format(movie[0], movie[1], movie[2]), end = "")
        stars = movie[3]

        for i, star in enumerate(stars):
            if i == len(stars) - 1:
                print(star)             #the last star
            else:
                print(star, end = ",") #the other stars
            print() #Skip a line


sys.exit(0)

