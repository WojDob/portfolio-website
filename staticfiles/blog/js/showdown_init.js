// Initialize Showdown on HTML containers with
// the .markdown2html class.
$(document).ready(function() {
  var converter = new showdown.Converter()
  $('.markdown2html').each(function() {
    var text = $(this).text();
    html = converter.makeHtml(text);
    $(this).html(html);
  });
});