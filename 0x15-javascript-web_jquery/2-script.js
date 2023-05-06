// Use jQuery to select header element
const elem = $('header');
$('#red_header').on('click', (event) => {
  elem.css('color', '#FF0000'); // Change color
});