// Use jQuery to hold list_movies
const elem = $('ul#list_movies');

// Use AJAX to get star wars films
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (movies) => {
    $.each(movies.results, (idx, movie) => {
      elem.append(`<li>${movie.title}</li>`);
    });
  },
  error: function () {
    alert('Error loading titles!');
  }
});
