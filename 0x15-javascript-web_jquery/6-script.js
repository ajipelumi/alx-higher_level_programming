// Use jQuery to select header element
const elem = $('header');
$('#update_header').on('click', (event) => {
  elem.text('New Header!!!');
});
