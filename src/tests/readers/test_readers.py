"""
Тестирование функций чтения данных из источника.
"""
from typing import Any
from openpyxl.workbook import Workbook

import pytest


from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    RegulationActModel,
    ThesisModel,
)

from readers.reader import (
    BookReader,
    InternetResourceReader,
    ArticlesCollectionReader,
    RegulationActReader,
    ThesisReader,
    SourcesReader,
)
from settings import TEMPLATE_FILE_PATH


class TestReaders:
    """
    Тестирование функций чтения данных из источника.
    """

    @pytest.fixture
    def workbook(self) -> Workbook:
        """
         Получение объекта тестовой рабочей книги.
        :return:
        """

        return SourcesReader(TEMPLATE_FILE_PATH).workbook

    def test_book(self, workbook: Workbook) -> None:
        """
        Тестирование чтения книги.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = BookReader(workbook).read()

        assert len(models) == 4
        model = models[0]

        model_type = BookModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.title == "Наука как искусство"
        assert model.edition == "3-е"
        assert model.city == "СПб."
        assert model.publishing_house == "Просвещение"
        assert model.year == 2020
        assert model.pages == 999

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_internet_resource(self, workbook: Workbook) -> None:
        """
        Тестирование чтения интернет-ресурса.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = InternetResourceReader(workbook).read()

        assert len(models) == 3
        model = models[0]

        model_type = InternetResourceModel

        assert isinstance(model, model_type)
        assert model.article == "Наука как искусство"
        assert model.website == "Ведомости"
        assert model.link == "https://www.vedomosti.ru"
        assert model.access_date == "01.01.2021"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 4

    def test_articles_collection(self, workbook: Workbook) -> None:
        """
        Тестирование чтения сборника статей.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = ArticlesCollectionReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = ArticlesCollectionModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article_title == "Наука как искусство"
        assert model.collection_title == "Сборник научных трудов"
        assert model.city == "СПб."
        assert model.publishing_house == "АСТ"
        assert model.year == 2020
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_regulation_act(self, workbook: Workbook) -> None:
        """
        Тестирование чтения нормативного акта.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = RegulationActReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = RegulationActModel

        assert isinstance(model, model_type)
        assert model.type == "Конституция Российской Федерации"
        assert model.title == "Наука как искусство"
        assert model.accept_date == "01.01.2000"
        assert model.number == "1234-56"
        assert model.official_source == "Парламентская газета"
        assert model.publication_year == 2020
        assert model.version == 5
        assert model.article_number == 15
        assert model.edition == "11.09.2002"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 9

    def test_thesis(self, workbook: Workbook) -> None:
        """
        Тестирование чтения диссертации.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = ThesisReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = ThesisModel

        assert isinstance(model, model_type)
        assert model.author == "Иванов И.М."
        assert model.title == "Наука как искусство"
        assert model.degree == "д-р. / канд."
        assert model.field == "экон."
        assert model.field_code == "01.01.01"
        assert model.city == "СПб."
        assert model.year == 2020
        assert model.pages == 199

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 8

    def test_sources_reader(self) -> None:
        """
        Тестирование функции чтения всех моделей из источника.
        """

        models = SourcesReader(TEMPLATE_FILE_PATH).read()
        # проверка общего считанного количества моделей
        assert len(models) == 10

        # проверка наличия всех ожидаемых типов моделей среди типов считанных моделей
        model_types = {model.__class__.__name__ for model in models}
        assert model_types == {
            BookModel.__name__,
            InternetResourceModel.__name__,
            ArticlesCollectionModel.__name__,
            RegulationActModel.__name__,
            ThesisModel.__name__,
        }
