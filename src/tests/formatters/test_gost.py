"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    RegulationActModel,
    ThesisModel,
)
from formatters.styles.gost import (
    GOSTBook,
    GOSTInternetResource,
    GOSTCollectionArticle,
    GOSTRegulationAct,
    GOSTThesis,
    GOSTCitationFormatter,
)


class TestGOST:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = GOSTBook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство. – 3-е изд. – СПб.: Просвещение, 2020. – 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = GOSTInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство // Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = GOSTCollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Сборник научных трудов. – СПб.: АСТ, 2020. – С. 25-30."
        )

    def test_thesis(self, thesis_fixture: ThesisModel) -> None:
        """
        Тестирование форматирования диссертации.
        :param ThesisModel thesis_fixture: Фикстура модели диссертации
        :return:
        """

        model = GOSTThesis(thesis_fixture)

        assert (
            model.formatted
            == "Иванов И.М. Наука как искусство : д-р. / канд. экон. 01.01.01 / СПб., 2020. - 999 с."
        )

    def test_regulation_act(self, regulation_act_fixture: RegulationActModel) -> None:
        """
        Тестирование форматирования нормативного акта.
        :param RegulationActModel regulation_act_fixture: Фикстура модели нормативного акта
        :return:
        """

        model = GOSTRegulationAct(regulation_act_fixture)

        assert (
            model.formatted
            == "Наука как искусство: Федеральный закон от 01.01.2021. №123: в ред. от 01.01.2021 // Научный журнал 2020"
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        regulation_act_fixture: RegulationActModel,
        thesis_fixture: ThesisModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param RegulationActModel regulation_act_fixture: Фикстура модели нормативного акта
        :param ThesisModel thesis_fixture: Фикстура модели диссертации
        :return:
        """

        models = [
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
            GOSTRegulationAct(regulation_act_fixture),
            GOSTThesis(thesis_fixture),
        ]

        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[4]
        assert result[1] == models[2]
        assert result[2] == models[0]
        assert result[3] == models[1]
        assert result[4] == models[3]
