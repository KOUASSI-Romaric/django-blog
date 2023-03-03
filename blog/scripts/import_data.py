from blog.models import Article


def run():
    for i in range(5, 15):
        article = Article()
        article.title = f'Article {i}'
        article.desc = f"Description de l'article n°{i}"
        article.image = "http://default"
        article.save()

    print("Opération réussit")
