(function () {
  var script = document.currentScript;
  var target = document.getElementById('site-banner');
  if (!script || !target) {
    return;
  }

  fetch(new URL('banner.html', script.src))
    .then(function (response) {
      if (!response.ok) {
        throw new Error('Banner could not be loaded');
      }
      return response.text();
    })
    .then(function (html) {
      target.outerHTML = html;
    })
    .catch(function (error) {
      console.error(error);
    });
})();
