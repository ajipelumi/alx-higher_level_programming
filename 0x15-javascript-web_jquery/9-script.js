$(document).ready(function () {
  // Use jQuery to hold hello
  const elem = $('#hello');

  // Use AJAX to get value of hello
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (data) => {
      elem.text(data.hello);
    }
  });
});
