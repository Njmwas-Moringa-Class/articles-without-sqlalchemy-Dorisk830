# #!/usr/bin/env python3

import sys
sys.path.append('lib')

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
        
    author1 = Author("Mwandishi Maarufu")
    author2 = Author("Mshairi Bora")

    magazine1 = Magazine("Hadithi za Kiafrika", "Fasihi")
    magazine2 = Magazine("Utamaduni Wetu", "Fasihi")

    article1 = author1.add_article(magazine1, "Machozi ya Simba")
    article2 = author2.add_article(magazine1, "Jua Limeshangaza")
    article3 = author1.add_article(magazine2, "Nyota Nyeusi")

    # Test

    # print("\nArticles:")
    # for article in Article.all():
    #     print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")
    
    # print("\nMagazines:")
    # for magazine in Magazine.all():
    #     print(f"{magazine.name()} - {magazine.category()}")

    # print("Authors:")
    # for author in Author.all():
    #     print(author.name())
    print("\nArticles:")
    for index, article in enumerate(Article.all(), start=1):
        print(f"{index}. {article.title()} by {article.author().name()} in {article.magazine().name()}")

    print("\nMagazines:")
    for index, magazine in enumerate(Magazine.all(), start=1):
        print(f"{index}. {magazine.name()} - {magazine.category()}")

    print("\nAuthors:")
    for index, author in enumerate(Author.all(), start=1):
        print(f"{index}. {author.name()}")

    
    
    ipdb.set_trace()
