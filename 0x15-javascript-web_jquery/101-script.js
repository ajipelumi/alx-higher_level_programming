$(document).ready(() => {
  // Use jQuery to select my_list element
  const elem = $('ul.my_list');

  $('#add_item').on('click', (event) => {
    elem.append('<li>Item</li>'); // Add item to list
  });

  $('#remove_item').on('click', (event) => {
    $('ul.my_list :last-child').remove(); // Remove last item from list
  });

  $('#clear_list').on('click', (event) => {
    elem.empty(); // Clear list
  });
});
