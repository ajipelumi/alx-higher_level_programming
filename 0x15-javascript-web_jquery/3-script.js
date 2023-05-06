// Use jQuery to select header element
const elem = $('header');
$('#red_header').on('click', (event) => {
  elem.addClass('red'); // Add class
});