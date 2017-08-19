import media
import fresh_tomatoes

the_dark_tower = media.Movie("The Dark Tower",
                  "A cowboy and a kid must seek out the man in black in the Dark Tower",
                  "http://cdn.collider.com/wp-content/uploads/2017/03/the-dark-tower-poster.jpg",
                  "https://www.youtube.com/watch?v=GjwfqXTebIY")

emoji_movie = media.Movie("Emoji Movie",
                          "An emoji wishes to display more than just their emotion and it causes problems",
                          "https://cdn.traileraddict.com/content/columbia-pictures/emoji-movie-poster-3.jpg",
                          "https://www.youtube.com/watch?v=1xv_FeBGzfk")

dunkirk = media.Movie("Dunkirk",
                      "A deeper look at one of historical moments from World War 2",
                      "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

atomic_blonde = media.Movie("Atomic Blonde",
                            "Following the most elite female MI6 spy as she travels into the heart of Berlin after the wall falls",
                            "https://s-media-cache-ak0.pinimg.com/originals/e1/a4/23/e1a4230933116bb7b8d295255eb39a21.jpg",
                            "https://www.youtube.com/watch?v=nI7HVnZlleo")

detroit = media.Movie("Detroit",
                      "Detailing the 1960s Detroit riots",
                      "http://www.impawards.com/2017/posters/detroit_xlg.jpg",
                      "https://www.youtube.com/watch?v=XzNrWGYzDZE")

spider_man = media.Movie("Spider-man: Homecoming",
                         "A young boy hero with spider like abilities tries to make a name for himself",
                         "http://www.impawards.com/2017/posters/spiderman_homecoming.jpg",
                         "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

nut_job2 = media.Movie("The Nut Job 2:",
                        "Surly the squirrel and his animal friends spring into action when the evil mayor of Oakton plans to bulldoze the park that they live in.",
                        "http://www.calandbob.com/wp-content/uploads/2016/06/The_Nut_Job_2-1.jpg",
                        "https://www.youtube.com/watch?v=e5qIZ89hj_A")

annabelle = media.Movie("Annabelle: Creation",
                        "A toy maker's daughter dies and the the family is gripped by horror when a little girl finds a doll in the attic.",
                        "https://cdn.traileraddict.com/content/warner-bros-pictures/annabelle-2-poster.jpg",
                        "https://www.youtube.com/watch?v=KisPhy7T__Q")

glass_castle = media.Movie("The Glass Castle",
                            "The life of a poor family that is always on the move",
                            "https://pre04.deviantart.net/9fa2/th/pre/i/2016/154/6/d/the_glass_castle__movie_poster__by_blantonl98-da4ug3p.jpg",
                            "https://www.youtube.com/watch?v=_eud7sJehLI")

kidnap = media.Movie("Kidnap",
                    "A woman will stop at nothing to get her child back",
                    "https://i2.wp.com/teaser-trailer.com/wp-content/uploads/Kidnap-movie-new-poster.jpg?ssl=1",
                    "https://www.youtube.com/watch?v=R-Ht8VRPRvU")

despicable3 = media.Movie("Despicable Me 3",
                        "A former villain and his brother find themselves confronting a new villain",
                        "https://movies.universalpictures.com/media/dm3-adv1sheet-rgb-5-58c818a68f809-1.png",
                        "https://www.youtube.com/watch?v=6DBi41reeF0")

hitmans_bodyguard = media.Movie("The Hitman's Bodyguard",
                                "A bodyguard must do all he can to protect a hitman",
                                "http://www.joblo.com/newsimages1/hit-body-poster-small.jpg",
                                "https://www.youtube.com/watch?v=F4Afusxc2SM")

movies = [the_dark_tower, emoji_movie, dunkirk, atomic_blonde, detroit, spider_man, nut_job2, annabelle, glass_castle, kidnap, despicable3, hitmans_bodyguard]
fresh_tomatoes.open_movies_page(movies)
