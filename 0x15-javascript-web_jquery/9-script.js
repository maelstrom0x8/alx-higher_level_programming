// Fetch translation
const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(URL, function (data) {
  const value = data.hello;
  $('#hello').append(value);
});
