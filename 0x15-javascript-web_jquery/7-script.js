// Fetches a character name from the url

const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(URL, function (data) {
  const name = data.name;
  $('#character').append(name);
});
