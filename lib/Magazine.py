class Magazine:
    magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def all():
        return Magazine.magazines

    def contributors(self):
        return list(set(article.author() for article in self._articles))

    def add_article(self, author, title):
        from Article import Article
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.magazines for article in magazine._articles]

    @classmethod
    def contributing_authors(cls):
        return [author for magazine in cls.magazines for author in magazine.contributors() if len(author.articles()) > 2]