// Use jQuery to select my_list element
const elem = $('ul.my_list');
$('#add_item').on('click', (event) => {
  elem.append('<li>Item</li>'); // Add item to list
});
