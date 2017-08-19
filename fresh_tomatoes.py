import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes - Movies</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        .navbar {
            background-color: #673AB7;
            height: 50px;
            width:100%;
            -webkit-box-shadow: 0px 0px 5px 7px rgba(0,0,0,0.75);
            -moz-box-shadow: 0px 0px 5px 7px rgba(0,0,0,0.75);
            box-shadow: 0px 0px 5px 7px rgba(0,0,0,0.75);
        }

        body {
            padding-top: 80px;
            background-color: #232323;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 1000px;
            height: 1000px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        #trailer-video {
            width: 100%;
            height: 100%;
        }

        .movie-tile {
            display: inline-block;
            margin: 0px;
            padding-top: 20px;
            color: white;
        }

        .movie-tile:hover {
            display: inline-block;
            cursor: pointer;
            background: rgba(103, 58, 183, 1);
            background: -moz-linear-gradient(top, rgba(103, 58, 183, 1) 0%, rgba(49, 27, 146, 1) 50%, rgba(103, 58, 183, 1) 100%);
            background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(103, 58, 183, 1)), color-stop(50%, rgba(49, 27, 146, 1)), color-stop(100%, rgba(103, 58, 183, 1)));
            background: -webkit-linear-gradient(top, rgba(103, 58, 183, 1) 0%, rgba(49, 27, 146, 1) 50%, rgba(103, 58, 183, 1) 100%);
            background: -o-linear-gradient(top, rgba(103, 58, 183, 1) 0%, rgba(49, 27, 146, 1) 50%, rgba(103, 58, 183, 1) 100%);
            background: -ms-linear-gradient(top, rgba(103, 58, 183, 1) 0%, rgba(49, 27, 146, 1) 50%, rgba(103, 58, 183, 1) 100%);
            background: linear-gradient(to bottom, rgba(103, 58, 183, 1) 0%, rgba(49, 27, 146, 1) 50%, rgba(103, 58, 183, 1) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#673ab7', endColorstr='#673ab7', GradientType=0);
            -webkit-box-shadow: -1px -1px 20px 6px rgba(0, 0, 0, 0.75);
            -moz-box-shadow: -1px -1px 20px 6px rgba(0, 0, 0, 0.75);
            box-shadow: -1px -1px 20px 6px rgba(0, 0, 0, 0.75);
            color: white;
            border-radius: 20px;
            text-shadow: 2px 2px black;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }

        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: #494A4B;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main page content -->
    <div class="container">
      <div class="navbar navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <img src="/Users/justinwilliams/Desktop/Python/Python/Movie-website/Movie-Project/tomato.ico" alt="Icon" height="45px" width="45px"  />
            <a class="navbar-brand" style="text-decoration:none; color:white; font-size:20px; text-shadow: 2px 2px black;" href="#"><strong>Fresh Tomatoes Movie Trailers</strong></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


#A single movie entry html template for the each of the movie tiles.  It will scale for 3 different screen sizes
movie_tile_content = '''
<div class="col-sm-6 col-md-4 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
