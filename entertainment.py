import media
import fresh_tomatoes

the_dark_tower = media.Movie("The Dark Tower",
                  "----",
                  "http://cdn.collider.com/wp-content/uploads/2017/03/the-dark-tower-poster.jpg",
                  "https://www.youtube.com/watch?v=GjwfqXTebIY")

emoji_movie = media.Movie("Emoji Movie",
                          "---",
                          "https://cdn.traileraddict.com/content/columbia-pictures/emoji-movie-poster-3.jpg",
                          "https://www.youtube.com/watch?v=1xv_FeBGzfk")

dunkirk = media.Movie("Dunkirk",
                      "---",
                      "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

atomic_blonde = media.Movie("Atomic Blonde",
                            "---",
                            "https://s-media-cache-ak0.pinimg.com/originals/e1/a4/23/e1a4230933116bb7b8d295255eb39a21.jpg",
                            "https://www.youtube.com/watch?v=nI7HVnZlleo")

detroit = media.Movie("Detroit",
                      "---",
                      "http://www.impawards.com/2017/posters/detroit_xlg.jpg",
                      "https://www.youtube.com/watch?v=XzNrWGYzDZE")

spider_man = media.Movie("Spider-man: Homecoming",
                         "A young boy hero with spider like abilities tries to make a name for himself",
                         "http://www.impawards.com/2017/posters/spiderman_homecoming.jpg",
                         "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

movies = [the_dark_tower, emoji_movie, dunkirk, atomic_blonde, detroit, spider_man]
fresh_tomatoes.open_movies_page(movies)

