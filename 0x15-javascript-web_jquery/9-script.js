$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  const translate = data.hello;
  $('#hello').text(translate);
});
