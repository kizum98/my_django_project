from django.core.management.base import BaseCommand

from web_form.models import Article

import csv


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        with open('articles.csv', 'w') as csv_file:
            fieldnames = ["ID",
                          "Заголовок",
                          "Автор",
                          "Дата",
                          "Рубрика",
                          "ID рубрики",
                          "Содержание",
                          "Ответ есть да/нет",
                          "Текст ответа",
                          "Фото есть да/нет"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for article in Article.objects.all():
                writer.writerow({fieldnames[0]: article.id,
                                 fieldnames[1]: article.title,
                                 fieldnames[2]: article.user_name,
                                 fieldnames[3]: article.date_send,
                                 fieldnames[4]: article.category,
                                 fieldnames[5]: article.category_id,
                                 fieldnames[6]: article.text,
                                 fieldnames[7]: "Да" if article.text_answer else "Нет",
                                 fieldnames[8]: article.text_answer,
                                 fieldnames[9]: "Да" if article.file else "Нет"})

        self.stdout.write(f"Done")
