var elements = document.querySelectorAll('a[href^="/news/articles/"]');
var articles = [];

elements.forEach(function(element) {
    var link = element.getAttribute('href');
    var title = element.textContent.trim();

    var article = {
        title: title,
        link: link
    };

    articles.push(article);
});

console.log(articles);
