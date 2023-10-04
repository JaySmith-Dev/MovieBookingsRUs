from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

available_movies = {  # Our movies are organised based on the movie_id of each item
    "1": {
        "title": "The Jungle Book (1967) (G)",
        "synopsis": "The boy Mowgli makes his way to the man-village with Bagheera, the wise panther. Along the way he meets jazzy King Louie, the hypnotic snake Kaa and the lovable, happy-go-lucky bear Baloo, who teaches Mowgli “The Bare Necessities” of life and the true meaning of friendship.",
        "ticket_price": 8.50,
        "tickets_remaining": 40,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/07/D100_DIGITAL_1SHEET_JUNGLE_BOOK_1330x1900-350x517.jpg",
        "image_loc": "/images/D100_DIGITAL_1SHEET_JUNGLE_BOOK_1330x1900-350x517.jpg",
        "release_date": "15/09/2023",
        "running_time": "78 minutes",
        "director": "Wolfgang Reitherman",
        "cast": "Louis Prima, Phil Harris, Sebastian Cabot",
    },
    "2": {
        "title": "Bolan's Shoes (15A)",
        "synopsis": "This story takes us on a tumultuous journey from the height of T. Rex mania in 1970s Liverpool to the present-day poignancy of what would have been Marc Bolan’s 75th birthday. It captures the heady exhilaration of glam rock mania through the experiences of a group of over-excited kids from a local children’s home before a devastating road accident changes their lives for ever. Years later, and still clinging to the adoration of her childhood idol, survivor Penny takes best friend and fellow Marc Bolan fan to visit his shrine in London but a chance encounter there catapults her back to the horror she had tried so hard to forget.",
        "ticket_price": 12.50,
        "tickets_remaining": 100,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/08/Featured-Bolans-shoes-350x525.jpg",
        "image_loc": "/images/Featured-Bolans-shoes-350x525.jpg",
        "release_date": "15/09/2023",
        "running_time": "95 minutes",
        "director": "Ian Puleston-Davies",
        "cast": "Leanne Best, Mark Lewis Jones, Timothy Spall",
    },
    "3": {
        "title": "A Haunting in Venice (12A)",
        "synopsis": "In post-World War II Venice, Poirot, now retired and living in his own exile, reluctantly attends a seance. But when one of the guests is murdered, it is up to the former detective to once again uncover the killer.",
        "ticket_price": 12.50,
        "tickets_remaining": 100,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/08/1Xgjl22MkAZQUavvOeBqRehrvqO-350x525.jpg",
        "image_loc": "/images/HauntingInVenice-350x525.jpg",
        "release_date": "15/09/2023",
        "running_time": "103 minutes",
        "director": "Kenneth Branagh",
        "cast": "Kelly Reilly, Kenneth Branagh, Michelle Yeoh",
    },
    "4": {
        "title": "Rally Road Racers (G)",
        "synopsis": "A rookie race-car driver gets the opportunity to compete against the reigning champion. With help from a former driver, he must overcome treacherous terrain, rival racers and unexpected obstacles to prove he has what it takes.",
        "ticket_price": 12.50,
        "tickets_remaining": 100,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/08/e9L7N5z3qHHgSNUIUuBSaicQvpT-350x525.jpg",
        "image_loc": "/images/RallyRoadRacers-350x525.jpg",
        "release_date": "15/09/2023",
        "running_time": "93 minutes",
        "director": "",
        "cast": "",
    },
    "5": {
        "title": "Rise of the Footsoldier: Vengeance (18)",
        "synopsis": "Pat Tate embarks on a rampage to avenge his loyal and trusted footsoldier’s violent death, venturing beyond his comfort zone of Essex into the dark side of 90s Soho to track down the villain responsible.",
        "ticket_price": 8.50,
        "tickets_remaining": 40,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/09/y1bqzVnGCZFYWvTkUBSfk6P2pkU-350x525.jpg",
        "image_loc": "/images/RiseOfTheFootSoldiers-350x525.jpg",
        "release_date": "15/09/2023",
        "running_time": "112 minutes",
        "director": "",
        "cast": "",
    },
    "6": {
        "title": "The Nun 2 (16)",
        "synopsis": "The horror thriller “The Nun II,” is the next chapter in the story of “The Nun,” the highest-grossing entry in the juggernaut $2 billion “The Conjuring” Universe.  1956 – France. A priest is murdered. An evil is spreading. The sequel to the worldwide smash hit follows Sister Irene as she once again comes face-to-face with Valak, the demon nun.",
        "ticket_price": 12.50,
        "tickets_remaining": 100,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/08/Featured-NUN-2-350x525.jpg",
        "image_loc": "/images/Featured-NUN-2-350x525.jpg",
        "release_date": "08/09/2023",
        "running_time": "104 minutes",
        "director": "Michael Chaves",
        "cast": "Anna Popplewell, Storm Reed, Taisse Farmiga",
    },
    "7": {
        "title": "My Big Fat Greek Wedding 3 (12A)",
        "synopsis": "Join the Portokalos family as they travel to a family reunion in Greece for a heartwarming and hilarious trip full of love, twists, and turns. Nia Vardalos returns to write, direct, and star in the third chapter that also brings John Corbett, Andrea Martin, Louis Mandylor, Maria Vacratsis, Elena Kampouris, Gia Carides, and Joey Fatone back to their roles. Elias Kacavas and Melina Kotselou complete the exciting ensemble for the unmissable big screen event. Opa!",
        "ticket_price": 10.00,
        "tickets_remaining": 70,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/08/irEqWPmDqCuzsItzefFxX3xWpL8-350x525.jpg",
        "image_loc": "/images/MyBigFatGreekWedding3-350x525.jpg",
        "release_date": "08/09/2023",
        "running_time": "92 minutes",
        "director": "Nia Vardalos",
        "cast": "Elena Kampouris, John Corbett, Louis Mandylor",
    },
    "8": {
        "title": "Past Lives (12A)",
        "synopsis": "Nora and Hae Sung, two deeply connected childhood friends, are wrested apart after Nora’s family emigrates from South Korea. Twenty years later, they are reunited for one fateful week as they confront notions of love and destiny.",
        "ticket_price": 10.00,
        "tickets_remaining": 70,
        "image_url": "https://www.movies-at.ie/wp-content/uploads/2023/09/gXt3eVpaBq6q9SaLDrgSnzsUyIl-350x525.jpg",
        "image_loc": "/images/PastLives-350x525.jpg",
        "release_date": "08/09/2023",
        "running_time": "106 minutes",
        "director": "Celine Song",
        "cast": "Greta Lee, John Magaro, Teo Yoo",
    }
}



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/contact')
def contact():
    return render_template("contact_us.html")

@app.route('/message_confirmation')
def message_confirmation():
    return render_template("message_confirmation.html")

@app.route('/subscribe_confirmation')
def subscribe_confirmation():
    return render_template("subscribe_confirmation.html")

@app.route('/movies/')
def movies():
    search_term = request.args.get("q", "")
    filtered_movies = []
    for movie_id, film in available_movies.items():
        if search_term.lower() in film["title"].lower() or search_term.lower() in film["synopsis"].lower():
            filtered_movies.append((movie_id, film))
    return render_template("movies.html", movies=filtered_movies)


@app.route('/film/<movie_id>')
def film(movie_id):
    return render_template("film.html", film=available_movies[movie_id], movie_id=movie_id)



@app.route('/order/<movie_id>', methods=["POST"])
def order(movie_id):
    film = available_movies[movie_id]
    if film["tickets_remaining"] > 0:
        film["tickets_remaining"] -= 1
        return render_template("order_confirmation.html")
    else:
        return "Sorry, there no tickets remaining for this movie"



if __name__ == '__main__':
    app.run(debug=True, port=8080)