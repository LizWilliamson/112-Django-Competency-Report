var movies = [];

function getCatalog(){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/movies',
        type: "GET",
        success: function(response){
            console.log("response from server", response);

            movies = response.objects;
            for(var i=0; i<movies.length; i++){
                var movie = movies[i];
                displayMovie(movie, i);
            }
        },
        error: function(errorDetails){
            conmsole.log("Error", errorDetails);
        }
    });

}

function displayMovie(movie, movie_count){
// get container
    var container = $("#container");
    var first = "active";
    if (movie_count>0){
        first="";
    }
    var indicator = `<li data-target="#carouselExampleCaptions" data-slide-to="${movie_count}" class="${first}"></li>`
    


//create html syntax
    var syntax = 
    `<div class="carousel-item ${first}">
        <img src="${movie.image_url}" class="d-block w-100">
        <div class="carousel-caption d-none d-md-block">
            <h5>Year: ${movie.release_year} | Genre: ${movie.genre.name}</h5>
            <h5>${movie.title}</h5>
            <h5>Star: ${movie.star}</h5>
            <h5>Director: ${movie.director}</h5>
        </div>
    </div>`;

    

 


//add syntax to container
container.append(syntax)
$(".carousel-indicators").append(indicator);
}





function init(){
    console.log("Catalog JS has loaded successfully!");

    getCatalog();
}

window.onload = init;