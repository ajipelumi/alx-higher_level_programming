// Use jQuery to select header element
const elem = $('header');
$('#toggle_header').on('click', (event) => {
  elem.toggleClass('green red'); // Toggle class
});
