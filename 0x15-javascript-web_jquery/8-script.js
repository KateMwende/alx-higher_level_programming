$.getJSON('https://swapi-api.alx-tools.com/api/films/', function (data) {
  $(#list_movies).append(data.title);
})
