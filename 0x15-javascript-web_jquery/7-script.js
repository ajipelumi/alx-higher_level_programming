// Use jQuery to hold character
const elem = $('#character');

// Use AJAX to get star wars character
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (data) => {
    elem.text(data.name);
  }
});